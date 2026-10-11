# MoveInSync Play Store ratings: why they are low and what to fix first

Case study for the MoveInSync Forward Deployed Engineer role (drive TC.21569.2027.64403).
App studied: MoveInSync employee app, `com.moveinsync.ets`.

**Start here: [`Recommendation_Memo.docx`](Recommendation_Memo.docx)** (3 pages: findings, ranked fixes with owners and measures, method and limits).

## Findings in brief
- The store shows 4.64 stars (114,855 ratings). In the 8,000 most recent written reviews the mean is 3.71 (29.6% are 1-2 stars); the last 12 months are 3.83 / 27.0%, and the last 90 days are not better than the 90 before.
- In the last 12 months, 772 reviews gave 1-2 stars. The most common named cause is login and OTP trouble (106 reviews, 14%), then crashes (40), unreachable support (37) and driver or pickup problems (up to 56). About two thirds name no specific issue.
- Developer replies to reviews nearly stopped after 2024 (about 37% of 2024 reviews were answered, under 1% in 2026).
- Older headline complaints (map zoom, seat-belt prompt, forced rating screen) are rare in the last 12 months (5, 3 and 8 reviews).

## Answering "how are our Play Store ratings?" again
```bash
pip install -r requirements.txt
python scripts/refresh_monitoring.py     # re-collect, re-analyze, print a health check (alerts on a rise in 1-2 star share or a drop in the mean)
streamlit run dashboard/app.py           # trend, versions, issue table, review explorer
```
A GitHub Action (`.github/workflows/monitor_ratings.yml`) runs the refresh every Monday and commits the updated data. Set `ALERT_WEBHOOK_URL` to push the alert text to a Slack-style webhook.

## Repository layout
```
Recommendation_Memo.docx          the recommendation (read this first)
README.md
docs/methodology.md               data, method, assumptions, limits, tools
scripts/collect_reviews.py        public Play Store reviews -> data/raw/
scripts/analyze_reviews.py        clean + broad themes -> data/processed/, reports/figures/
scripts/issue_evidence.py         specific issue counts (last 12 months and all time)
scripts/refresh_monitoring.py     one-command refresh + health check
dashboard/app.py                  Streamlit dashboard
data/raw/                         collected reviews (reviewer names removed) + collection metadata
data/processed/                   cleaned reviews, metrics, issue_evidence.csv
reports/figures/                  charts
tests/test_analysis.py            pytest checks (cleaning, metrics, privacy, issue rules)
.github/workflows/                weekly refresh
```

## Run the tests
```bash
python -m pytest -q
```

## Honest limits
Issue counts come from keyword rules, not hand labelling, and reviews show symptoms rather than causes; see `docs/methodology.md`. An AI assistant (Claude) helped write the code and draft the memo.

Author: Ravi Ranjan. Licence: MIT.
