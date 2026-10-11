"""
MoveInSync Play Store Reviews Collector
Collects public Google Play reviews for a package (default: com.moveinsync.ets) into data/raw/
"""

import argparse
import datetime
import json
import os
import sys
import time
from typing import Dict, Any, List, Optional
import pandas as pd

try:
    from google_play_scraper import app as get_app_info, reviews, Sort
except ImportError:
    print("Error: google-play-scraper is not installed. Run `pip install google-play-scraper`.")
    sys.exit(1)


PRIMARY_APP_ID = "com.moveinsync.ets"
APP_STORE_BASE_URL = "https://play.google.com/store/apps/details?id="


def fetch_app_metadata(app_id: str, lang: str = "en", country: str = "in") -> Dict[str, Any]:
    """Fetch official store metadata including overall score, install count, and version."""
    try:
        info = get_app_info(app_id, lang=lang, country=country)
        return {
            "app_id": app_id,
            "title": info.get("title", ""),
            "developer": info.get("developer", ""),
            "current_store_score": round(info.get("score", 0.0), 4) if info.get("score") else None,
            "store_ratings_count": info.get("ratings", 0),
            "store_reviews_count": info.get("reviews", 0),
            "installs": info.get("installs", ""),
            "app_version": info.get("version", ""),
            "store_url": f"{APP_STORE_BASE_URL}{app_id}",
            "status": "success"
        }
    except Exception as exc:
        print(f"[Warning] Failed to fetch app store metadata for {app_id}: {exc}")
        return {
            "app_id": app_id,
            "store_url": f"{APP_STORE_BASE_URL}{app_id}",
            "status": f"failed: {str(exc)}"
        }


def collect_reviews(
    app_id: str = PRIMARY_APP_ID,
    target_count: int = 5000,
    lang: str = "en",
    country: str = "in",
    delay_between_batches: float = 0.5
) -> List[Dict[str, Any]]:
    """
    Collect reviews from Google Play Store across both NEWEST and MOST_RELEVANT sorting
    to capture both fresh operational regressions and high-impact historical issues.
    """
    collected_dict: Dict[str, Dict[str, Any]] = {}
    sort_modes = [
        ("NEWEST", Sort.NEWEST),
        ("MOST_RELEVANT", Sort.MOST_RELEVANT)
    ]

    print(f"[*] Starting review collection for: {app_id} (Target: {target_count} reviews)...")

    for sort_label, sort_enum in sort_modes:
        print(f"[*] Querying stream with sort order: {sort_label}...")
        continuation_token = None
        consecutive_empty = 0

        while len(collected_dict) < target_count:
            try:
                batch_size = min(1000, target_count - len(collected_dict))
                if batch_size <= 0:
                    break

                batch_reviews, continuation_token = reviews(
                    app_id,
                    lang=lang,
                    country=country,
                    sort=sort_enum,
                    count=batch_size,
                    continuation_token=continuation_token
                )

                if not batch_reviews:
                    consecutive_empty += 1
                    if consecutive_empty >= 2:
                        print(f"[-] No more reviews returned for {sort_label}.")
                        break
                    continue
                else:
                    consecutive_empty = 0

                initial_len = len(collected_dict)
                for rev in batch_reviews:
                    r_id = rev.get("reviewId")
                    if r_id and r_id not in collected_dict:
                        collected_dict[r_id] = rev

                added = len(collected_dict) - initial_len
                print(f"    Fetched batch of {len(batch_reviews)} ({added} new unique). Total collected: {len(collected_dict)}")

                if not continuation_token:
                    print(f"[-] End of pagination token for {sort_label}.")
                    break

                time.sleep(delay_between_batches)

            except Exception as e:
                print(f"[!] Error encountered while collecting {sort_label} reviews: {e}")
                break

    return list(collected_dict.values())


def normalize_raw_records(records: List[Dict[str, Any]], app_id: str, redact_names: bool = True) -> pd.DataFrame:
    """Normalize raw scraper output into clean tabular DataFrame format, redacting reviewer names by default."""
    normalized = []
    for r in records:
        review_date = r.get("at")
        if isinstance(review_date, datetime.datetime):
            date_str = review_date.isoformat()
        else:
            date_str = str(review_date) if review_date else ""

        reply_date = r.get("repliedAt")
        if isinstance(reply_date, datetime.datetime):
            reply_date_str = reply_date.isoformat()
        else:
            reply_date_str = str(reply_date) if reply_date else ""

        user_display_name = "[REDACTED]" if redact_names else (r.get("userName", "") or "")

        normalized.append({
            "review_id": r.get("reviewId", ""),
            "app_id": app_id,
            "user_name": user_display_name,
            "rating": int(r.get("score", 0)),
            "review_text": r.get("content", "") or "",
            "review_date": date_str,
            "app_version": r.get("reviewCreatedVersion") or r.get("appVersion") or "",
            "thumbs_up_count": int(r.get("thumbsUpCount", 0)),
            "developer_reply": r.get("replyContent") or "",
            "reply_date": reply_date_str
        })

    df = pd.DataFrame(normalized)
    return df


def import_csv_workflow(import_path: str, app_id: str) -> pd.DataFrame:
    """Fallback workflow to import external CSV data if online scraping is restricted."""
    print(f"[*] Importing external reviews dataset from: {import_path}")
    df = pd.read_csv(import_path)

    # Column mapping heuristics
    mapping = {
        "reviewId": "review_id",
        "userName": "user_name",
        "score": "rating",
        "content": "review_text",
        "at": "review_date",
        "reviewCreatedVersion": "app_version",
        "thumbsUpCount": "thumbs_up_count",
        "replyContent": "developer_reply"
    }
    df = df.rename(columns=mapping)

    required_cols = ["review_id", "user_name", "rating", "review_text", "review_date", "app_version", "thumbs_up_count"]
    for col in required_cols:
        if col not in df.columns:
            df[col] = "" if col != "rating" and col != "thumbs_up_count" else 0

    df["app_id"] = app_id
    return df


def main():
    parser = argparse.ArgumentParser(description="Collect public Google Play reviews for a package.")
    parser.add_argument("--app-id", type=str, default=PRIMARY_APP_ID, help="Google Play package name")
    parser.add_argument("--target-count", type=int, default=5000, help="Maximum number of unique reviews to collect")
    parser.add_argument("--lang", type=str, default="en", help="Language code (default: en)")
    parser.add_argument("--country", type=str, default="in", help="Country code (default: in)")
    parser.add_argument("--output-dir", type=str, default="data/raw", help="Target directory for raw data")
    parser.add_argument("--import-csv", type=str, default=None, help="Import reviews from local CSV instead of scraping")
    parser.add_argument("--keep-user-names", action="store_true", help="Preserve public reviewer display names (default: False / redacted for privacy)")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    collection_start = datetime.datetime.now(datetime.timezone.utc).isoformat()

    # 1. Fetch official store metadata
    meta = fetch_app_metadata(args.app_id, lang=args.lang, country=args.country)

    # 2. Collect reviews or import
    if args.import_csv and os.path.exists(args.import_csv):
        df_raw = import_csv_workflow(args.import_csv, args.app_id)
        collection_method = "manual_csv_import"
    else:
        raw_records = collect_reviews(
            app_id=args.app_id,
            target_count=args.target_count,
            lang=args.lang,
            country=args.country
        )
        if not raw_records:
            print("[!] Collection returned zero reviews. Please verify network access or use --import-csv.")
            sys.exit(1)
        df_raw = normalize_raw_records(raw_records, args.app_id, redact_names=not args.keep_user_names)
        collection_method = "google_play_scraper_api"

    # 3. Save raw CSV
    app_slug = args.app_id.replace(".", "_")
    raw_csv_path = os.path.join(args.output_dir, f"reviews_raw_{app_slug}.csv")
    df_raw.to_csv(raw_csv_path, index=False, encoding="utf-8")
    print(f"[+] Saved {len(df_raw)} raw reviews to: {raw_csv_path}")

    # 4. Save metadata summary
    min_date = df_raw["review_date"].min() if not df_raw.empty else None
    max_date = df_raw["review_date"].max() if not df_raw.empty else None

    metadata_payload = {
        "collection_timestamp_utc": collection_start,
        "collection_method": collection_method,
        "app_id": args.app_id,
        "app_title": meta.get("title", "MoveInSync"),
        "developer": meta.get("developer", "MoveInSync: Enabling Hybrid Workplaces"),
        "current_store_score": meta.get("current_store_score"),
        "store_ratings_count": meta.get("store_ratings_count"),
        "store_reviews_count": meta.get("store_reviews_count"),
        "installs": meta.get("installs"),
        "store_url": meta.get("store_url"),
        "collected_sample_size": len(df_raw),
        "date_range": {
            "earliest_review_date": str(min_date),
            "latest_review_date": str(max_date)
        },
        "query_parameters": {
            "language": args.lang,
            "country": args.country,
            "target_count": args.target_count
        },
        "collection_limitations": [
            "Google Play Store restricts bulk public scraping to accessible paginated review tokens (~3,000-8,000 reviews).",
            "Data reflects English-language reviews primarily submitted from the India region (IN).",
            "Private employee feedback submitted directly via in-app corporate transport desk tickets is internal and not represented in Play Store public data.",
            "Historical reviews where users uninstalled without reviewing or rated via star-only without text are partially unrepresented in qualitative analysis."
        ]
    }

    meta_json_path = os.path.join(args.output_dir, f"collection_metadata_{app_slug}.json")
    with open(meta_json_path, "w", encoding="utf-8") as f:
        json.dump(metadata_payload, f, indent=2)
    print(f"[+] Saved collection metadata to: {meta_json_path}")

    # Also save standard collection_metadata.json for convenience
    std_meta_path = os.path.join(args.output_dir, "collection_metadata.json")
    with open(std_meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata_payload, f, indent=2)


if __name__ == "__main__":
    main()
