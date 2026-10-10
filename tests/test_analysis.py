"""
Unit and Integration Tests for MoveInSync Reviews Analysis Pipeline
Author: Forward Deployed Engineer (FDE) Candidate
"""

import json
import os
import pandas as pd
import pytest
from scripts.analyze_reviews import clean_dataset, calculate_metrics, THEME_DEFINITIONS


@pytest.fixture
def sample_raw_df():
    """Create a controlled synthetic raw DataFrame for deterministic testing."""
    records = [
        {
            "review_id": "rev-001",
            "app_id": "com.moveinsync.ets",
            "user_name": "Test User 1",
            "rating": 1,
            "review_text": "worst app ever! Map keeps zooming out every 3 seconds while tracking the cab.",
            "review_date": "2026-05-10T12:00:00Z",
            "app_version": "12.19.0",
            "thumbs_up_count": 12,
            "developer_reply": "",
            "reply_date": ""
        },
        {
            "review_id": "rev-002",
            "app_id": "com.moveinsync.ets",
            "user_name": "Test User 2",
            "rating": 2,
            "review_text": "When I click view otp, it pops up seat belt safety warning. Very annoying!",
            "review_date": "2026-05-11T08:30:00Z",
            "app_version": "12.19.0",
            "thumbs_up_count": 5,
            "developer_reply": "Thank you for feedback",
            "reply_date": "2026-05-12T09:00:00Z"
        },
        {
            "review_id": "rev-003",
            "app_id": "com.moveinsync.ets",
            "user_name": "Test User 3",
            "rating": 5,
            "review_text": "Excellent service and safe commute every day. Highly recommended!",
            "review_date": "2026-05-12T14:15:00Z",
            "app_version": "12.18.0",
            "thumbs_up_count": 2,
            "developer_reply": "",
            "reply_date": ""
        },
        {
            "review_id": "rev-004",
            "app_id": "com.moveinsync.ets",
            "user_name": "Test User 4",
            "rating": 3,
            "review_text": "Good app but please add dark mode and fix minor delay.",
            "review_date": "2026-05-13T10:00:00Z",
            "app_version": "12.19.0",
            "thumbs_up_count": 0,
            "developer_reply": "",
            "reply_date": ""
        },
        # Duplicate record
        {
            "review_id": "rev-001",
            "app_id": "com.moveinsync.ets",
            "user_name": "Test User 1 Duplicate",
            "rating": 1,
            "review_text": "worst app ever! Map keeps zooming out every 3 seconds while tracking the cab.",
            "review_date": "2026-05-10T12:00:00Z",
            "app_version": "12.19.0",
            "thumbs_up_count": 12,
            "developer_reply": "",
            "reply_date": ""
        }
    ]
    return pd.DataFrame(records)


def test_clean_dataset_deduplication(sample_raw_df):
    """Test that duplicate review_id records are properly dropped."""
    df_clean = clean_dataset(sample_raw_df)
    assert len(df_clean) == 4
    assert df_clean["review_id"].tolist() == ["rev-001", "rev-002", "rev-003", "rev-004"]


def test_sentiment_classification(sample_raw_df):
    """Test that ratings are correctly categorized into Positive, Neutral, Negative."""
    df_clean = clean_dataset(sample_raw_df)
    sentiments = dict(zip(df_clean["review_id"], df_clean["sentiment"]))
    assert sentiments["rev-001"] == "Negative"
    assert sentiments["rev-002"] == "Negative"
    assert sentiments["rev-003"] == "Positive"
    assert sentiments["rev-004"] == "Neutral"


def test_theme_classification_rules(sample_raw_df):
    """Test regex pattern tagging for GPS and OTP friction themes."""
    df_clean = clean_dataset(sample_raw_df)

    # rev-001 mentions map zooming out and tracking
    r1 = df_clean[df_clean["review_id"] == "rev-001"].iloc[0]
    assert r1["theme_gps_live_tracking"] == 1
    assert r1["theme_general_dissatisfaction"] == 1

    # rev-002 mentions view otp and seat belt
    r2 = df_clean[df_clean["review_id"] == "rev-002"].iloc[0]
    assert r2["theme_otp_notifications"] == 1

    # rev-003 mentions excellent service and safe commute
    r3 = df_clean[df_clean["review_id"] == "rev-003"].iloc[0]
    assert r3["theme_positive_commute_experience"] == 1


def test_calculate_metrics(sample_raw_df):
    """Test aggregation math in calculate_metrics."""
    df_clean = clean_dataset(sample_raw_df)
    metrics = calculate_metrics(df_clean)

    summary = metrics["summary"]
    assert summary["total_reviews"] == 4
    assert summary["total_negative_reviews"] == 2
    assert summary["negative_review_rate_pct"] == 50.0
    assert summary["average_rating"] == pytest.approx(2.75, 0.01)
    assert summary["sentiment_counts"]["Negative"] == 2
    assert summary["sentiment_counts"]["Positive"] == 1
    assert summary["sentiment_counts"]["Neutral"] == 1


def test_processed_files_exist_and_valid():
    """Verify that actual generated project artifacts exist and have valid structure."""
    processed_csv = "data/processed/reviews_cleaned.csv"
    metrics_json = "data/processed/analysis_metrics.json"
    pdf_report = "reports/MoveInSync_FDE_Case_Study.pdf"

    assert os.path.exists(processed_csv), f"Missing {processed_csv}"
    assert os.path.exists(metrics_json), f"Missing {metrics_json}"
    assert os.path.exists(pdf_report), f"Missing {pdf_report}"

    df = pd.read_csv(processed_csv)
    assert len(df) == 8000
    assert "rating" in df.columns
    assert "sentiment" in df.columns
    assert "theme_gps_live_tracking" in df.columns

    with open(metrics_json, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["summary"]["total_reviews"] == 8000
    assert data["summary"]["average_rating"] == pytest.approx(3.707, 0.01)
