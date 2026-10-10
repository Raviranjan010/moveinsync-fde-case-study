# Data Collection & Analysis Methodology

**MoveInSync Forward Deployed Engineer (FDE) Candidate Case Study**  
**Investigation Target:** MoveInSync Employee Commute Mobile App (`com.moveinsync.ets`)

---

## 1. Research Objectives & Strategic Context

MoveInSync is the world’s leading employee commute and workplace automation platform, powering daily mobility for over **1.5 million enterprise employees** across **430+ organizations** in 39 countries. 

While the Google Play Store displays a cumulative historical rating of **4.64★** (aggregated over 114,000+ ratings since app inception), qualitative analysis of recent user reviews reveals an active **dissatisfaction rate of 29.61%** (1-star and 2-star reviews).

The objective of this research is to:
1. Systematically collect genuine, publicly accessible user reviews from the Google Play Store.
2. Filter, clean, and deduplicate reviews to build an empirical, un-manipulated dataset.
3. Classify user friction points into validated operational and engineering themes.
4. Separate measured review symptoms from unverified internal root-cause hypotheses.
5. Provide actionable, prioritized engineering and product recommendations that can be executed immediately by MoveInSync engineering teams.

---

## 2. Scope of Analysis & App Ecosystem Segmentation

MoveInSync maintains multiple distinct applications on the Google Play Store designed for specific operational roles:

| Application Package ID | App Name | Primary User Persona | Store Rating | Included in Scope? | Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`com.moveinsync.ets`** | **MoveInSync** | **Enterprise Employees** | **~4.64★** | **YES (Primary)** | Direct employee touchpoint for self-booking, live cab tracking, boarding OTPs, and shift rosters. This is where brand sentiment is won or lost. |
| `com.moveinsync.driver.lite` | Moveinsync Partner - Lite | Cab Drivers & Fleet Partners | ~4.25★ | Excluded from primary corpus | Operational navigation, trip sheet execution, and passenger validation. Separate driver persona. |
| `com.moveinsync.driver.dco` | MoveInSync - Driver Partner | Fleet Driver Partners | ~3.50★ | Excluded from primary corpus | Dedicated driver-partner workflow; distinct operational failure modes (incentives, trip allocation). |
| `field.moveinsync.ets` | MoveInSync - Field app | Transport Marshals & Desk Operations | ~4.08★ | Excluded from primary corpus | Internal on-premise operational tooling; low review volume. |

> **Scope Rule:** Do not mix employee, driver, and workplace app reviews without explaining the distinction. This case study focuses strictly on `com.moveinsync.ets` to diagnose the exact user journey of corporate commuters.

---

## 3. Data Collection Architecture & Provenance

Data was collected using the Python `google-play-scraper` library, interacting directly with public Google Play Store endpoints without requiring authenticated scraping or proprietary internal access.

### Collection Parameters:
* **Target Package Identifier:** `com.moveinsync.ets`
* **Target Sample Size:** 8,000 unique reviews
* **Sorting Strategies Used:** Both `Sort.NEWEST` (to capture recent software regressions and post-update bugs) and `Sort.MOST_RELEVANT` (to capture high-impact issues endorsed by community upvotes).
* **Language & Regional Scope:** `lang='en'`, `country='in'` (India, MoveInSync's primary operational market).
* **Collection Timestamp:** October 2026.
* **Effective Date Range:** December 15, 2023 to October 09, 2026.

### Raw Data Schema:
Each collected review record captures the following empirical fields:
* `review_id`: Globally unique Google Play Store review UUID.
* `user_name`: Display name of reviewer.
* `rating`: Integer star score from 1 to 5.
* `review_text`: Unmodified text feedback written by user.
* `review_date`: Timestamp of review submission (ISO 8601).
* `app_version`: App build version installed by user at time of review (e.g. `12.19.0`, `12.20.0`).
* `thumbs_up_count`: Number of other Play Store users who marked the review as helpful.
* `developer_reply`: Official MoveInSync customer support response text (if present).
* `reply_date`: Timestamp of developer response.

---

## 4. Data Cleaning & Transformation Pipeline

The data processing pipeline (`scripts/analyze_reviews.py`) executes deterministic cleaning stages:

```
[Raw Google Play Scraper] 
       │ (8,000 records)
       ▼
[Deduplication Engine] ──────────► Deduplicate by review_id
       │
       ▼
[Text Normalization] ────────────► Strip whitespace, handle NaN, compute length & word counts
       │
       ▼
[Date & Version Parsing] ────────► Parse UTC datetimes, extract Year-Month, normalize version strings
       │
       ▼
[Sentiment Segmentation] ────────► 1-2★: Negative | 3★: Neutral | 4-5★: Positive
       │
       ▼
[Thematic Pattern Engine] ───────► Multi-label regex matching across 11 validated themes
       │
       ▼
[Processed Clean Dataset] ───────► Saved to data/processed/reviews_cleaned.csv
```

### Sentiment Classification Definitions:
* **Negative (Detractor):** Ratings of `1` or `2` stars. These represent active friction, broken workflows, or product dissatisfaction.
* **Neutral (Passive):** Rating of `3` stars. Mixed experiences or feature suggestions.
* **Positive (Promoter):** Ratings of `4` or `5` stars. Successful, safe, and punctual commutes.

---

## 5. Thematic Categorization Taxonomy

Thematic classification is multi-label: a single review can mention multiple issues (for example, cab delay and inaccurate GPS tracking simultaneously). 

The classification taxonomy was constructed and validated using iterative token frequency analysis, n-gram co-occurrence, and manual spot-checking against genuine negative reviews:

| Theme Key | Human Label | Regex Boundary Logic & Keywords |
| :--- | :--- | :--- |
| `app_performance_crash` | App Crashes & Performance | Crashes, app freezing, blank screen, stuck on splash screen, uninstall/reinstall, slow loading, stopped working. |
| `gps_live_tracking` | GPS & Live Tracking Glitches | Inaccurate ETA, map auto-zooms out, frozen vehicle marker, routing errors, wrong vehicle position, navigation delay. |
| `booking_roster_flow` | Booking & Roster Flow | Self-booking failure, slot cut-off times, waitlist lack of feedback, confusion between login/logout shift timings. |
| `vehicle_delay_pickup` | Pickup Delays & Cab No-Show | Cab delayed 45-60 min, late pickup, excessive curb waiting, cab not assigned, missed cab. |
| `driver_behavior_safety` | Driver Conduct & Commute Safety | Rash driving, speeding, rude behavior, AC turned off, unauthorized driver, night safety concerns. |
| `login_roster_account` | Login, SSO & Session Expiry | Frequent automatic logouts, corporate SSO credential errors, session expired, unable to log in before shift. |
| `otp_notifications` | OTP & Notification Friction | Seatbelt popup blocking "View OTP", delayed OTP SMS, missing arrival notification, push alert spam. |
| `ui_usability_prompts` | UI Usability & Forced Rating | Forced post-ride rating dialog with no skip button, confusing UI redesigns, clunky navigation. |
| `support_desk_operations` | Support Desk & Issue Resolution | Transport desk unresponsive, tickets closed without solution, lack of real-time human escalation. |
| `general_dissatisfaction` | General Dissatisfaction | Generic venting without feature citation ("worst app", "pathetic", "third class", "waste of time"). |
| `positive_commute_experience`| Positive Commute Feedback | Punctual, safe, comfortable, smooth ride, great driver, convenient corporate transport. |

---

## 6. Analytical Guardrails & Limitations

1. **Empirical Symptoms vs Root Causes**:  
   Public reviews report observable symptoms (e.g., *"the map zooms out every 3 seconds"*, *"app crashed after update"*). We strictly label internal architectural explanations as **hypotheses** requiring validation via internal telemetry (crash logs, APM traces, backend API latency metrics).
2. **Review Self-Selection Bias**:  
   Users who experience friction are significantly more motivated to write long, detailed public reviews than satisfied riders who simply tap 5 stars or don't review. This explains why the review corpus has a higher negative concentration (29.61%) than the cumulative store rating (4.64★).
3. **Regional & Language Scope**:  
   Collection was scoped to English reviews originating from India (`country='in'`). Regional vernacular expressions in Hindi/Hinglish (e.g., *bekar*, *bakwas*) were mapped into general dissatisfaction.
