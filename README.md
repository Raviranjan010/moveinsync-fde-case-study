# MoveInSync | Play Store Rating Intelligence & Prioritized Fixes

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/tests-7%20passed-brightgreen.svg)]()
[![Streamlit Dashboard](https://img.shields.io/badge/dashboard-Streamlit-red.svg)](https://streamlit.io/)
[![PDF Report](https://img.shields.io/badge/report-PDF%20Generated-navy.svg)]()
[![Presentation](https://img.shields.io/badge/presentation-PPTX%20Deck-orange.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Forward Deployed Engineer (FDE) Candidate Case Study Assignment**  
> **Investigation Target:** MoveInSync Employee Commute Mobile App (`com.moveinsync.ets`)  
> **Corpus Analyzed:** $N_{total} = 8,000$ Genuine Verified Reviews (Dec 2023 – Oct 2026)  
> **Public GitHub Repository:** [https://github.com/Raviranjan010/moveinsync-fde-case-study](https://github.com/Raviranjan010/moveinsync-fde-case-study)  

---

## 1. Executive Summary

MoveInSync powers daily commute logistics for over **1.5 million enterprise employees** across **430+ Fortune 500 organizations**. While the Google Play Store India listing displays a cumulative historical rating of **4.64★** (114,867 ratings), empirical analysis of **8,000 verified public written reviews** reveals that **29.61% of written reviews are negative (1★ or 2★)**, with 1-star reviews alone accounting for **26.17% (2,094 reviews)** and pulling the written sample average rating to **3.71★**.

An exhaustive data audit confirms that low ratings are **not caused by systemic platform rejection**, but by **three critical, localized software friction points** occurring at time-sensitive curbside boarding moments:
1. **Boarding OTP Latency (P0):** A blocking seatbelt safety modal intercepts the "View OTP" action, forcing curbside boarding delays and driver conflict.
2. **Maps SDK Auto-Zoom Glitch (P0):** Live tracking automatically resets camera bounds and zooms out every 3–4 seconds, overriding user pinch zoom (highest community upvotes: **428 upvotes**).
3. **Forced In-App Rating Dialog (P0):** An unskippable post-trip rating prompt locks users out of the app, driving frustrated riders straight to the Play Store to leave retaliatory 1-star reviews.

Deploying targeted hotfixes for these three **P0 items in Sprint 1** will immediately halt the negative review cycle, protect MoveInSync's corporate reputation, and uplift daily employee sentiment.

---

## 2. Storefront Baseline Rating Reconciliation

During technical review, an apparent contradiction surfaced between the report's 4.64★ lifetime store rating and external evaluations of ~4.3★. This is **empirically resolved by Google Play Store's regional localization policy**:

| Storefront / Locale | Displayed Rating | Ratings / Reviews Sampled | User Persona Context |
| :--- | :---: | :---: | :--- |
| **India (`gl=IN`)** | **4.64★** (`4.6381`) | 114,867 ratings / 23,619 reviews | **Primary corporate employee commute base (>99% of rides)** |
| **United States (`gl=US`)** | **4.32★** (~4.3★) | 100 reviews | US-based enterprise travelers and external review evaluators |
| **Great Britain (`GB`)** | **4.49★** | 26 reviews | UK enterprise employees |
| **Philippines (`PH`)** | **4.49★** | 281 reviews | BPO client employees |
| **Partner Driver Lite App** | **4.25★** (~4.3★) | 7,280 reviews | Driver Partner Lite (`com.moveinsync.driver.lite`) |
| **Written Review Sample** | **3.71★** | 8,000 written reviews | Sample mean reflects **negative selection bias** of written text reviews |

* **Localization Policy:** In late 2021, Google Play localized star ratings by user country and device type. Reviewers on US accounts see **4.32★**, while users in India see the canonical **4.64★**.
* **Written Sample vs Store Score:** The store rating aggregates silent 1-tap star ratings. The collected sample contains only **written text reviews**, which naturally exhibit a lower mean (**3.71★**) due to negative self-selection bias.

---

## 3. Repository Architecture

```
moveinsync-fde-case-study/
│
├── .github/workflows/
│   └── monitor_ratings.yml       # Weekly CI/CD rating refresh workflow (proposed)
│
├── data/
│   ├── raw/                      # Genuine raw scraper outputs & metadata
│   │   ├── reviews_raw_com_moveinsync_ets.csv  # 8,000 reviews (PII-redacted)
│   │   └── collection_metadata.json
│   └── processed/                # Cleaned, deduplicated dataset & metrics
│       ├── reviews_cleaned.csv   # 8,000 processed reviews (PII-redacted)
│       └── analysis_metrics.json # Full statistical aggregations & reconciliation
│
├── scripts/
│   ├── collect_reviews.py        # Google Play scraper with PII redaction by default
│   ├── analyze_reviews.py        # Data cleaning, theme taxonomy & figure generator
│   ├── generate_pdf_report.py    # ReportLab publication-grade PDF builder
│   ├── generate_presentation.py # python-pptx executive 10-slide presentation builder
│   └── refresh_monitoring.py     # Repeatable refresh, pipeline runner & local alerting
│
├── dashboard/
│   └── app.py                    # Interactive Streamlit analytics dashboard
│
├── reports/
│   ├── MoveInSync_FDE_Case_Study.pdf          # 4-page publication-ready PDF report
│   ├── MoveInSync_FDE_Case_Study.md           # Full comprehensive markdown report
│   ├── MoveInSync_Case_Study_Presentation.pptx # 10-slide executive presentation deck
│   ├── analysis_summary.md                    # Core analytical findings summary
│   └── figures/                               # High-res visualization charts
│       ├── figure1_rating_distribution.png
│       ├── figure2_rating_trends_over_time.png
│       ├── figure3_complaint_themes_frequency.png
│       └── figure4_theme_severity_vs_frequency.png
│
├── docs/
│   ├── data_verification.md                   # Full audit of IDs, provenance & baseline
│   ├── classification_validation_worksheet.md # 30-review worksheet for human review
│   ├── methodology.md                         # Collection provenance, taxonomy & disclosures
│   └── recommendations.md                     # Prioritized matrix, risks & roadmap
│
├── tests/
│   └── test_analysis.py          # Pytest suite validating math, PII, and deliverables
│
├── requirements.txt              # Production Python dependencies
├── pytest.ini                    # Test runner configuration
├── .gitignore                    # Local materials (reference/, data/backup/) excluded
└── README.md                     # Comprehensive project documentation
```

---

## 4. Quick Start & Setup Instructions

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

## 5. Execution Commands

### A. Run Automated Tests
```powershell
pytest -v
```
*Validates data cleaning, sentiment assignment, regex rules, metric math, PII redaction, deliverable artifacts, and the 30-review validation worksheet (7/7 tests passing).*

### B. Clean Data, Classify Themes & Generate Visualizations
```powershell
python scripts/analyze_reviews.py
```
*Processes `data/raw/reviews_raw_com_moveinsync_ets.csv`, outputs `data/processed/reviews_cleaned.csv`, `data/processed/analysis_metrics.json`, and saves figures in `reports/figures/`.*

### C. Launch Interactive Streamlit Dashboard
```powershell
streamlit run dashboard/app.py
```
*Launches an interactive web dashboard in your browser at `http://localhost:8501` featuring KPI cards, charts, real review explorer, and recommendation filters.*

### D. Compile Formal Multi-Page PDF Report
```powershell
python scripts/generate_pdf_report.py
```
*Compiles the publication-ready formal report to `reports/MoveInSync_FDE_Case_Study.pdf`.*

### E. Compile Executive PowerPoint Presentation Deck
```powershell
python scripts/generate_presentation.py
```
*Compiles the 10-slide executive presentation to `reports/MoveInSync_Case_Study_Presentation.pptx`.*

### F. Run Repeatable Rating Monitoring Pipeline
```powershell
python scripts/refresh_monitoring.py
```
*Runs the full refresh pipeline: review scraping, analysis, PDF compilation, presentation generation, and console regression alerting (with optional webhook dispatch via `ALERT_WEBHOOK_URL`).*

---

## 6. Summary of Empirical Findings

* **Total Reviews Analyzed ($N_{total}$):** **8,000 genuine reviews**
* **Negative Detractors ($N_{neg}$):** **2,369 reviews rated 1★ or 2★ (29.61%)**
* **Positive Promoters ($N_{pos}$):** **5,388 reviews rated 4★ or 5★ (67.35%)**
* **Neutral Passives ($N_{neu}$):** **243 reviews rated 3★ (3.04%)**
* **Sample Review Corpus Mean Rating:** **3.707★**
* **Multi-Label Overlap:** Total theme citations in negative reviews = 6,210 (percentages sum to **262.14%** across negative reviews).

### Star Rating Distribution ($N = 8,000$)
| Star Rating | Volume | Percentage Share | Sentiment Segment |
| :---: | :---: | :---: | :--- |
| **1★** | **2,094** | **26.17%** | Negative (High Detractor) |
| **2★** | **275** | **3.44%** | Negative (Moderate Detractor) |
| **3★** | **243** | **3.04%** | Neutral (Passive) |
| **4★** | **654** | **8.18%** | Positive (Promoter) |
| **5★** | **4,734** | **59.17%** | Positive (High Promoter) |

### Top Complaint Themes in Negative Reviews ($N_{neg} = 2,369$)
| Theme | Negative Reviews | % of Negatives | Mean Score | Community Upvotes | Priority |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **App Crashes & Performance** | 462 | 19.50% | 1.90★ | 280 | **P1** |
| **GPS & Live Tracking Glitches** | 372 | 15.70% | 2.62★ | **428 (Highest)** | **P0** |
| **Booking & Roster Flow** | 273 | 11.52% | 2.39★ | 303 | **P1** |
| **Pickup Delays & Cab No-Show** | 252 | 10.64% | 2.28★ | 263 | **P1** |
| **Login, SSO & Session Expiry** | 227 | 9.58% | **1.47★ (Lowest)** | 150 | **P1** |
| **Driver Conduct & Commute Safety** | 215 | 9.08% | 2.21★ | 361 | **P2** |
| **OTP & Notification Friction** | 207 | 8.74% | 1.90★ | 208 | **P0** |
| **Support Desk & Escalation Issues** | 139 | 5.87% | 1.77★ | 115 | **P2** |
| **UI Usability & Forced Rating Prompts**| 131 | 5.53% | 1.78★ | 236 | **P0** |

---

## 7. Prioritized Recommendation Matrix

| ID | Priority | Theme | Recommended Action | Affected Volume | Responsible Team | Success Metric |
| :--- | :---: | :--- | :--- | :---: | :--- | :--- |
| **REC-01** | **P0** | OTP Friction | Render persistent OTP chip; decouple seatbelt popup into non-blocking animation. | 207 / 2,369 (8.7%) | Mobile App Squad, UX | Boarding OTP view latency (<0.5s) |
| **REC-02** | **P0** | GPS Tracking | Decouple cab marker coordinate updates from camera animation bounding; add re-center FAB. | 372 / 2,369 (15.7%) | Maps SDK Squad | Auto-reset interrupts = 0 |
| **REC-03** | **P0** | Rating Prompts | Add prominent Skip button on ride rating card; auto-dismiss on inactivity. | 131 / 2,369 (5.5%) | Product Design | Retaliatory 1★ review rate |
| **REC-04** | **P1** | Session / Auth | Silent background OAuth2 token refresh worker; crash-safe Room DB migrations. | 227 / 2,369 (9.6%) | Mobile Platform | Involuntary logout rate (<1.0%) |
| **REC-05** | **P1** | ETA Accuracy | Dynamic traffic layer integration; display arrival confidence windows. | 252 / 2,369 (10.6%) | Routing Algorithms | ETA MAE <= 5 min |
| **REC-06** | **P1** | Booking Flow | Human-centered copy ('To Office' / 'To Home'); cutoff countdown timers. | 273 / 2,369 (11.5%) | Product Design | Self-booking funnel drop-off |
| **REC-07** | **P2** | Support Desk | In-app issue bot with 1-tap quick actions and live client marshal escalation. | 139 / 2,369 (5.9%) | FDE & Ops Tech | First Response Time (<2 min) |
| **REC-08** | **P2** | Driver Safety | Post-ride AC feedback chips; driver telematics speed monitoring loop. | 215 / 2,369 (9.1%) | Driver Ecosystem | Overspeeding / 1,000 km |

---

## 8. Telemetry Boundaries, Data Hygiene & AI Tools Disclosure

* **Symptom vs Root-Cause Boundary:** Public Play Store reviews report observable user symptoms (e.g., *"the map zooms out every 3 seconds"*, *"app crashed after update"*). Underlying technical explanations are framed as engineering hypotheses requiring validation via internal APM (Crashlytics, Datadog).
* **Enterprise Privacy Protection:** Reviewer display names (`user_name`) have been redacted (`[REDACTED]`) in public repository files to protect end-user personal information.
* **Permitted AI Assistance Disclosure:** In alignment with assignment instructions (*"Use any tools you like, AI included"*), AI coding assistants were utilized for exploratory regex structuring, test generation, and slide compilation scripts. All mathematical aggregations, data verifications, and recommendations were verified through deterministic code and documented worksheets.

---

## 9. Deliverables & Submission Checklist

- [x] **Verified Raw & Processed Datasets:** `data/raw/` and `data/processed/` with PII redaction.
- [x] **Data Verification Audit Document:** `docs/data_verification.md` with baseline reconciliation.
- [x] **Manual Validation Worksheet:** `docs/classification_validation_worksheet.md` (30 representative reviews with blank validation fields).
- [x] **Data Collection Script:** `scripts/collect_reviews.py` with PII redaction by default.
- [x] **Data Analysis Script:** `scripts/analyze_reviews.py` with multi-label tagging and chart generator.
- [x] **Interactive Dashboard:** `dashboard/app.py` built with Streamlit.
- [x] **Formal PDF Report:** `reports/MoveInSync_FDE_Case_Study.pdf` (ReportLab).
- [x] **Comprehensive Markdown Report:** `reports/MoveInSync_FDE_Case_Study.md`.
- [x] **Executive Presentation Deck:** `reports/MoveInSync_Case_Study_Presentation.pptx` (python-pptx).
- [x] **Methodology & Recommendations:** `docs/methodology.md` and `docs/recommendations.md`.
- [x] **Repeatable Monitoring Pipeline:** `scripts/refresh_monitoring.py` and `.github/workflows/monitor_ratings.yml`.
- [x] **Automated Test Suite:** `tests/test_analysis.py` (7/7 passing).
- [x] **Repository Hygiene:** Reference files untracked from Git index; no secrets or personal credentials exposed.

---

## 10. Author & License

* **Candidate:** Raviranjan Kumar
* **Role:** Forward Deployed Engineer (FDE) Candidate
* **Target Company:** MoveInSync Technology Solutions Pvt Ltd
* **License:** [MIT License](LICENSE)