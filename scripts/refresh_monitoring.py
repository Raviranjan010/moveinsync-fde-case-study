"""
MoveInSync Ongoing Play Store Rating Monitoring Script
Author: Forward Deployed Engineer (FDE) Candidate
Purpose: Periodically refresh Google Play Store reviews, detect sentiment regressions,
         and trigger operational alerts if negative review volume spikes.
"""

import datetime
import json
import os
import subprocess
import sys


ALERT_THRESHOLD_NEGATIVE_RATE = 25.0  # Alert if >25% of recent reviews are 1-2 stars


def run_pipeline():
    print(f"[{datetime.datetime.now().isoformat()}] Starting MoveInSync Rating Refresh Workflow...")

    # Step 1: Collect latest reviews
    print("[1/3] Scraping fresh reviews from Google Play Store...")
    collect_cmd = [sys.executable, "scripts/collect_reviews.py", "--app-id", "com.moveinsync.ets", "--target-count", "8000"]
    ret1 = subprocess.run(collect_cmd, capture_output=True, text=True)
    if ret1.returncode != 0:
        print(f"[!] Collection failed: {ret1.stderr}")
        return False
    print("    Collection completed.")

    # Step 2: Re-run analysis & regenerate figures
    print("[2/3] Analyzing updated review corpus & generating visual metrics...")
    analyze_cmd = [sys.executable, "scripts/analyze_reviews.py"]
    ret2 = subprocess.run(analyze_cmd, capture_output=True, text=True)
    if ret2.returncode != 0:
        print(f"[!] Analysis failed: {ret2.stderr}")
        return False
    print("    Analysis completed.")

    # Step 3: Re-compile PDF report
    print("[3/4] Re-compiling updated PDF report...")
    pdf_cmd = [sys.executable, "scripts/generate_pdf_report.py"]
    ret3 = subprocess.run(pdf_cmd, capture_output=True, text=True)
    if ret3.returncode != 0:
        print(f"[!] PDF generation failed: {ret3.stderr}")
        return False
    print("    PDF report compiled.")

    # Step 4: Re-compile updated presentation deck (if script exists)
    if os.path.exists("scripts/generate_presentation.py"):
        print("[4/4] Re-generating PowerPoint presentation deck...")
        ppt_cmd = [sys.executable, "scripts/generate_presentation.py"]
        ret4 = subprocess.run(ppt_cmd, capture_output=True, text=True)
        if ret4.returncode == 0:
            print("    PowerPoint presentation compiled.")
        else:
            print(f"[Warning] Presentation generation had issues: {ret4.stderr}")

    # Health Check & Regression Alerting
    metrics_path = "data/processed/analysis_metrics.json"
    if os.path.exists(metrics_path):
        with open(metrics_path, "r", encoding="utf-8") as f:
            metrics = json.load(f)

        summary = metrics["summary"]
        neg_rate = summary["negative_review_rate_pct"]
        avg_score = summary["average_rating"]
        total = summary["total_reviews"]

        print("\n" + "=" * 60)
        print("          MOVEINSYNC RATINGS HEALTH MONITOR REPORT")
        print("=" * 60)
        print(f"Total Reviews in Database: {total:,}")
        print(f"Sample Average Rating:     {avg_score} Stars")
        print(f"Active Negative Rate:      {neg_rate}% (1-2 Star Reviews)")

        webhook_url = os.environ.get("ALERT_WEBHOOK_URL")
        if neg_rate > ALERT_THRESHOLD_NEGATIVE_RATE:
            alert_msg = f"[ALERT - REGRESSION DETECTED] Negative review share ({neg_rate}%) exceeds threshold ({ALERT_THRESHOLD_NEGATIVE_RATE}%).\nAction Required: Check P0 hotfix status (OTP modal, Map auto-zoom, Forced rating prompt)."
            print(f"\n{alert_msg}")
        else:
            alert_msg = f"[STATUS NORMAL] Negative review share is within acceptable boundary ({neg_rate}% <= {ALERT_THRESHOLD_NEGATIVE_RATE}%)."
            print(f"\n{alert_msg}")

        if webhook_url:
            print(f"[*] Dispatching webhook alert to configured endpoint...")
            try:
                import urllib.request
                req = urllib.request.Request(
                    webhook_url,
                    data=json.dumps({"text": alert_msg}).encode("utf-8"),
                    headers={"Content-Type": "application/json"}
                )
                urllib.request.urlopen(req, timeout=10)
                print("[+] Webhook alert dispatched successfully.")
            except Exception as w_err:
                print(f"[!] Webhook delivery failed: {w_err}")
        else:
            print("[Note] External webhook not configured (ALERT_WEBHOOK_URL unset). Console alerting active.")
        print("=" * 60 + "\n")

    return True


if __name__ == "__main__":
    success = run_pipeline()
    sys.exit(0 if success else 1)
