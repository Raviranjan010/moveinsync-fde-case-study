# MoveInSync | Play Store Rating Intelligence & Prioritized Fixes

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-5%20passed-brightgreen.svg)]()
[![Streamlit Dashboard](https://img.shields.io/badge/dashboard-Streamlit-red.svg)](https://streamlit.io/)
[![PDF Report](https://img.shields.io/badge/report-PDF%20Generated-navy.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Forward Deployed Engineer (FDE) Candidate Case Study Assignment**  
> **Investigation Target:** MoveInSync Employee Commute Mobile App (`com.moveinsync.ets`)  
> **Public GitHub Repository:** [https://github.com/Raviranjan010/moveinsync-fde-case-study](https://github.com/Raviranjan010/moveinsync-fde-case-study)

---

## 1. Executive Summary

MoveInSync powers workplace mobility for over **1.5 million enterprise employees** daily across **430+ enterprise customers** globally. While the Google Play Store displays a cumulative historical rating of **4.64★** (aggregated across 114,855 all-time star submissions), empirical analysis of **8,000 genuine written user reviews** reveals an active **dissatisfaction rate of 29.61%** (1-star and 2-star reviews), with 1-star reviews alone accounting for **26.17% (2,094 reviews)**.

The investigation demonstrates that low ratings are **not caused by systemic employee rejection of the platform**, but by **three critical, localized software friction points** during the curbside commute lifecycle:
1. **Boarding OTP Latency (P0):** A blocking seatbelt safety modal intercepts the "View OTP" action, forcing curbside boarding delays and driver conflict.
2. **Maps SDK Auto-Zoom Glitch (P0):** Live tracking automatically resets camera bounds and zooms out every 3 seconds, overriding user pinch zoom (highest community upvotes: **428 upvotes**).
3. **Forced In-App Rating Dialog (P0):** An unskippable post-trip rating prompt locks users out of the app, driving frustrated riders straight to the Play Store to leave retaliatory 1-star reviews.

Resolving these three **P0 hotfixes** will immediately halt the negative review cycle and uplift daily sentiment.

---

## 2. Repository Structure

```
moveinsync-fde-case-study/
│
├── .github/workflows/
│   └── monitor_ratings.yml       # Weekly CI/CD rating refresh & drift alert
│
├── data/
│   ├── raw/                      # Genuine raw scraper outputs & metadata
│   │   ├── reviews_raw_com_moveinsync_ets.csv
│   │   └── collection_metadata.json
│   └── processed/                # Cleaned, deduplicated dataset & metrics
│       ├── reviews_cleaned.csv
│       └── analysis_metrics.json
│
├── scripts/
│   ├── collect_reviews.py        # Google Play scraper & fallback CSV importer
│   ├── analyze_reviews.py        # Data cleaning, theme taxonomy & figure generator
│   ├── generate_pdf_report.py    # ReportLab publication-grade PDF builder
│   └── refresh_monitoring.py     # Repeatable refresh & threshold anomaly detector
│
├── dashboard/
│   └── app.py                    # Interactive Streamlit analytics dashboard
│
├── reports/
│   ├── MoveInSync_FDE_Case_Study.pdf # Publication-ready 4-page formal case study report
│   ├── analysis_summary.md       # Comprehensive markdown findings report
│   └── figures/                  # High-res visualization chart figures
│       ├── figure1_rating_distribution.png
│       ├── figure2_rating_trends_over_time.png
│       ├── figure3_complaint_themes_frequency.png
│       └── figure4_theme_severity_vs_frequency.png
│
├── docs/
│   ├── methodology.md            # Collection provenance, taxonomy & limitations
│   └── recommendations.md        # Full engineering specs, metrics & experiments
│
├── tests/
│   └── test_analysis.py          # Pytest suite validating cleaning & math logic
│
├── reference/                    # Original assignment PDF & JD documentation
│   ├── Case Study FDE Moveinsync.pdf
│   └── JD FDE Moevinsync.pdf
│
├── requirements.txt              # Production Python dependencies
├── pytest.ini                    # Test runner configuration
├── .gitignore                    # Python & environment exclusions
└── README.md                     # Comprehensive project documentation
```

---

## 3. Quick Start & Setup Instructions (Windows / Mac / Linux)

### Prerequisites
* Python 3.10+ (Tested on Python 3.12.10)
* Git

### Step-by-Step Installation:

```powershell
# 1. Clone the repository
git clone https://github.com/Raviranjan010/moveinsync-fde-case-study.git
cd moveinsync-fde-case-study

# 2. Create and activate a Python virtual environment
python -m venv .venv
# On Windows PowerShell:
.venv\Scripts\Activate.ps1
# On macOS / Linux:
source .venv/bin/activate

# 3. Install required dependencies
pip install -r requirements.txt

# 4. Run the automated test suite to verify installation
pytest -v
```

---

## 4. Execution Commands

### A. Collect Fresh Genuine Reviews
```powershell
# Scrapes up to 8,000 genuine reviews from Google Play Store for com.moveinsync.ets
python scripts/collect_reviews.py --app-id com.moveinsync.ets --target-count 8000
```
*Note: A complete pre-scraped dataset is already included in `data/raw/` so external scraping is optional.*

### B. Clean Data, Classify Themes & Generate Figures
```powershell
python scripts/analyze_reviews.py
```
*Generates `data/processed/reviews_cleaned.csv`, `data/processed/analysis_metrics.json`, and charts in `reports/figures/`.*

### C. Launch Interactive Streamlit Dashboard
```powershell
streamlit run dashboard/app.py
```
*Opens an interactive web dashboard in your browser at `http://localhost:8501` featuring KPI cards, charts, review explorer, and recommendation filters.*

### D. Compile Formal Multi-Page PDF Report
```powershell
python scripts/generate_pdf_report.py
```
*Compiles the publication-ready formal report to `reports/MoveInSync_FDE_Case_Study.pdf`.*

### E. Run Ongoing Rating Monitoring & Anomaly Detection
```powershell
python scripts/refresh_monitoring.py
```

---

## 5. Summary of Empirical Findings

* **Total Reviews Analyzed:** 8,000 genuine reviews
* **Store Cumulative Lifetime Score:** 4.638★ (114,855 ratings)
* **Sample Review Corpus Mean Rating:** 3.707★
* **Positive Reviews (4-5★):** 5,388 (67.35%)
* **Negative Reviews (1-2★):** 2,369 (29.61%)
* **Neutral Reviews (3★):** 243 (3.04%)

### Star Rating Breakdown
| Star Rating | Volume | Percentage Share | Sentiment Segment |
| :---: | :---: | :---: | :--- |
| **1★** | **2,094** | **26.17%** | Negative (High Detractor) |
| **2★** | **275** | **3.44%** | Negative (Moderate Detractor) |
| **3★** | **243** | **3.04%** | Neutral (Passive) |
| **4★** | **654** | **8.18%** | Positive (Promoter) |
| **5★** | **4,734** | **59.18%** | Positive (High Promoter) |

### Top Negative Complaint Themes ($N_{neg} = 2,369$)
| Theme | Negative Reviews | % of Negatives | Mean Score | Community Upvotes | Priority |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **App Crashes & Performance** | 462 | 19.5% | 1.90★ | 280 | **P1** |
| **GPS & Live Tracking Glitches** | 372 | 15.7% | 2.62★ | **428** | **P0** |
| **Booking & Roster Flow** | 273 | 11.5% | 2.39★ | 303 | **P1** |
| **Pickup Delays & Cab No-Show** | 252 | 10.6% | 2.28★ | 263 | **P1** |
| **Login, SSO & Session Expiry** | 227 | 9.6% | **1.47★** | 150 | **P1** |
| **Driver Conduct & Commute Safety** | 215 | 9.1% | 2.77★ | 361 | **P2** |
| **OTP & Notification Friction** | 207 | 8.7% | 1.90★ | 208 | **P0** |
| **Support Desk & Issue Resolution** | 139 | 5.9% | 1.77★ | 115 | **P2** |
| **UI Usability & Forced Rating Prompts** | 131 | 5.5% | 3.61★ | 236 | **P0** |

---

## 6. Prioritized Recommendations Matrix

| ID | Priority | Theme | Recommended Action | Affected Volume | Responsible Team | Success Metric |
| :--- | :---: | :--- | :--- | :---: | :--- | :--- |
| **REC-01** | **P0** | OTP & Notifications | Eliminate OTP latency; decouple blocking seatbelt modal into non-intrusive banner. | 207 (8.7%) | Android App Squad, UX | Boarding OTP view latency (&lt;1s) |
| **REC-02** | **P0** | GPS & Live Tracking | Fix Google Maps SDK camera auto-zoom / reset loop during live cab tracking. | 372 (15.7%) | Android Maps Squad | Camera auto-reset events / session |
| **REC-03** | **P0** | UI & Rating Prompts | Remove forced ride rating modal; introduce explicit "Skip" button. | 131 (5.5%) | Product Design, App Squad | Play Store 1-star retaliatory rate |
| **REC-04** | **P1** | Login & Auth | Implement silent OAuth2 token refresh; add crash-safe database migration routines. | 227 (9.6%) | Mobile Platform, Auth Backend | Involuntary logout rate (&lt;1%) |
| **REC-05** | **P1** | Pickup Delays / ETA | Traffic-aware dynamic ETA calibration with confidence arrival intervals. | 252 (10.6%) | Routing Algorithms, Data Eng | ETA Error Margin ($\le$ 5 min) |
| **REC-06** | **P1** | Booking Flow | Human-centered shift commute terminology ("To Office" / "To Home"). | 273 (11.5%) | Product Design, Mobile Squad | Self-booking funnel drop-off |
| **REC-07** | **P2** | Support Desk | In-app live dispatch escalation bot with automated trip status checks. | 139 (5.9%) | Forward Deployed Eng (FDE) | First Response Time (&lt;2 min) |
| **REC-08** | **P2** | Driver & Safety | Driver AC and speeding compliance telematics feedback loop. | 215 (9.1%) | Driver Ecosystem, Safety Ops | Speeding events / 1,000 km |

---

## 7. Telemetry Boundaries & Limitations

* **Symptom vs Root-Cause Boundary:** Public Play Store reviews describe observable user symptoms (e.g., *"app crashed after update"*, *"map zoomed out"*). Root causes (e.g. database schema migration conflicts, maps camera boundary listeners) are hypotheses requiring validation via internal APM (Crashlytics, Datadog).
* **Enterprise SLA Tickets:** Private feedback submitted directly to corporate enterprise transport desks is not reflected in public store data.

---

## 8. Verification & Test Suite

The test suite validates data cleaning, deduplication, sentiment classification, theme tagging, and statistical aggregation:
```powershell
pytest -v
```
Output:
```
============================= test session starts =============================
platform win32 -- Python 3.12.10, pytest-9.1.1
tests/test_analysis.py::test_clean_dataset_deduplication PASSED          [ 20%]
tests/test_analysis.py::test_sentiment_classification PASSED             [ 40%]
tests/test_analysis.py::test_theme_classification_rules PASSED           [ 60%]
tests/test_analysis.py::test_calculate_metrics PASSED                    [ 80%]
tests/test_analysis.py::test_processed_files_exist_and_valid PASSED      [100%]
============================== 5 passed in 2.26s ==============================
```

---

## 9. Deliverables & Submission Checklist

- [x] **Raw & Processed Datasets:** Stored in `data/raw/` and `data/processed/`.
- [x] **Data Collection Script:** `scripts/collect_reviews.py` with CSV fallback.
- [x] **Data Analysis Script:** `scripts/analyze_reviews.py` with theme classification.
- [x] **Interactive Dashboard:** `dashboard/app.py` built with Streamlit.
- [x] **Formal PDF Report:** `reports/MoveInSync_FDE_Case_Study.pdf` (4 pages, ReportLab).
- [x] **Markdown Reports:** `reports/analysis_summary.md`, `docs/methodology.md`, `docs/recommendations.md`.
- [x] **Automated Monitoring:** `scripts/refresh_monitoring.py` and `.github/workflows/monitor_ratings.yml`.
- [x] **Unit Tests:** `tests/test_analysis.py` (5/5 tests passing).
- [x] **Dependencies:** `requirements.txt`.
- [x] **Git Cleanliness:** No passwords, tokens, API keys, or personal secrets.

---

## 10. Author & License

* **Candidate:** Raviranjan Kumar
* **Role:** Forward Deployed Engineer (FDE) Candidate
* **Target Company:** MoveInSync Technology Solutions Pvt Ltd
* **License:** [MIT License](LICENSE)