# Methodology

## Question
Why are the Play Store ratings for MoveInSync lower than they should be, and what should be fixed first?

## Scope
- App: `com.moveinsync.ets` (MoveInSync employee app), the app employees use to book and track rides.
- Not covered: the driver app and the field app; reviews in languages other than English; reviews from outside the India storefront.

## Data
- Source: public Google Play reviews, collected with the `google-play-scraper` Python library (`scripts/collect_reviews.py`).
- Collected on 10 Oct 2026: the 8,000 most recent written reviews (of about 23,600), dated 15 Dec 2023 to 9 Oct 2026. Settings: language `en`, country `in`.
- Store score at collection time: 4.6377 stars from 114,855 ratings (`data/raw/collection_metadata.json`).
- Reviewer display names are replaced with `[REDACTED]` before anything is saved.

## Steps
1. `scripts/analyze_reviews.py` cleans and de-duplicates reviews, adds sentiment buckets (1-2 negative, 3 neutral, 4-5 positive) and broad theme tags, and writes `data/processed/` and `reports/figures/`.
2. `scripts/issue_evidence.py` counts specific, fixable issues in 1-2 star reviews with keyword rules, for the last 365 days and for all time. Run it with `--samples 5` to print random matches for every rule and check them by eye.
3. The memo (`Recommendation_Memo.docx`) ranks issues by how many negative reviews name them in the last 12 months, then by how much the app team can fix directly.

## Why the last 12 months
Almost all 2026 reviews are on version 12.x, while many of the most upvoted complaints come from version 11.x in 2024. Using all-time counts would point the team at problems that may already be fixed.

## Limits
- Written reviews are a small, negative-leaning slice of riders, so their mean (about 3.8) is lower than the store score (4.64). Trends in this sample are more useful than the absolute level.
- Issue counts come from keyword rules, not human labels. A review can match several issues, some matches are wrong, and reviews written in other words are missed. About two thirds of negative reviews mention no specific issue, so every count is a lower bound for that issue.
- Reviews show symptoms, not causes. The fixes in the memo are hypotheses to check against internal crash, OTP and ticket data.
- Developer reply data is as returned by the scraper.

## Tools
Python 3, pandas, matplotlib, Streamlit, pytest, GitHub Actions. An AI assistant (Claude) helped write the scripts and draft the memo; all numbers can be regenerated with the scripts in this repository.
