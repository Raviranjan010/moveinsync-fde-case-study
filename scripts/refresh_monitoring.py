"""Refresh the Play Store ratings picture and flag regressions.

Runs: collect -> analyze -> issue evidence -> health check.
Run it any time someone asks "how are our Play Store ratings?" (the GitHub
Action in .github/workflows runs it every Monday).

Optional: set ALERT_WEBHOOK_URL (Slack-style webhook) to push the alert text.
"""
import datetime
import json
import os
import subprocess
import sys
import urllib.request

import pandas as pd

APP_ID = "com.moveinsync.ets"
NEG_RATE_ALERT = 30.0      # alert if >30% of last-90-day written reviews are 1-2 stars
MEAN_DROP_ALERT = 0.20     # alert if last-90-day mean falls this far below the prior 90 days


def run(step: str, cmd: list) -> None:
    print(f"[{datetime.datetime.now():%H:%M:%S}] {step}")
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-1500:])
        sys.exit(f"Step failed: {step}")


def health_check() -> str:
    df = pd.read_csv("data/processed/reviews_cleaned.csv", parse_dates=["review_date"])
    end = df["review_date"].max()
    last = df[df["review_date"] > end - pd.Timedelta(days=90)]
    prev = df[(df["review_date"] <= end - pd.Timedelta(days=90)) &
              (df["review_date"] > end - pd.Timedelta(days=180))]
    neg_rate = 100 * (last["rating"] <= 2).mean()
    lines = [
        f"Last 90 days: {len(last)} written reviews, mean {last['rating'].mean():.2f}, "
        f"{neg_rate:.1f}% are 1-2 stars",
        f"Prior 90 days: {len(prev)} reviews, mean {prev['rating'].mean():.2f}, "
        f"{100 * (prev['rating'] <= 2).mean():.1f}% are 1-2 stars",
    ]
    neg = last[last["rating"] <= 2]
    lines.append(f"Developer reply rate on 1-2 star reviews (last 90 days): "
                 f"{100 * neg['developer_reply'].notna().mean():.1f}%")
    alerts = []
    if neg_rate > NEG_RATE_ALERT:
        alerts.append(f"negative share {neg_rate:.1f}% > {NEG_RATE_ALERT}%")
    if prev["rating"].mean() - last["rating"].mean() > MEAN_DROP_ALERT:
        alerts.append("mean rating dropped vs prior 90 days")
    lines.append("ALERT: " + "; ".join(alerts) if alerts else "Status: within thresholds")
    return "\n".join(lines)


def main() -> None:
    run("Collecting reviews", [sys.executable, "scripts/collect_reviews.py",
                               "--app-id", APP_ID, "--target-count", "8000"])
    run("Analyzing themes", [sys.executable, "scripts/analyze_reviews.py"])
    run("Counting issues", [sys.executable, "scripts/issue_evidence.py"])
    report = health_check()
    print("\n" + report)
    hook = os.environ.get("ALERT_WEBHOOK_URL")
    if hook:
        req = urllib.request.Request(hook, data=json.dumps({"text": report}).encode(),
                                     headers={"Content-Type": "application/json"})
        try:
            urllib.request.urlopen(req, timeout=10)
        except Exception as exc:  # alerting must never break the refresh
            print("Webhook failed:", exc)


if __name__ == "__main__":
    main()
