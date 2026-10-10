# MoveInSync Play Store Reviews Analysis Summary

**Project:** Forward Deployed Engineer (FDE) Candidate Case Study  
**Subject:** Google Play Store Rating Investigation & Action Plan for MoveInSync (`com.moveinsync.ets`)  
**Data Extraction Date:** October 2026 | **Corpus Size:** 8,000 Genuine Reviews

---

## 1. Executive Summary

MoveInSync powers workplace mobility for over **1.5 million employees** daily across **430+ enterprise customers**. While the cumulative lifetime Play Store rating stands at **4.64★** (based on 114,855 historical ratings), analysis of genuine user reviews reveals that **29.61% of written reviews are negative (1★ or 2★)**, with 1-star reviews alone accounting for **26.17% (2,094 reviews)**.

The empirical analysis indicates that poor ratings are **not caused by generalized platform dissatisfaction**, but by **specific, high-friction moments during the daily commute lifecycle**:

1. **Boarding OTP Latency (P0)**: A blocking seatbelt modal intercepts the "View OTP" action, forcing curbside delays and driver arguments.
2. **Maps Camera Auto-Zoom Glitch (P0)**: The Google Maps tracking screen automatically resets camera bounds every 3 seconds, overriding user zoom gestures (highest community upvotes: 428 upvotes).
3. **Forced In-App Rating Dialog (P0)**: An unskippable post-trip rating prompt locks users out of the app, driving retaliatory 1-star reviews to the Play Store.
4. **App Crashes & Auth Drops Post-Update (P1)**: 462 reviews cite app freezes or forced logouts after version updates, requiring manual reinstallation.
5. **Static ETA Discrepancy vs City Traffic (P1)**: Severe divergence between in-app arrival estimates and real Google Maps traffic.

---

## 2. Quantitative Summary Metrics

| Metric Dimension | Value | Notes / Context |
| :--- | :--- | :--- |
| **Total Reviews Collected** | **8,000** | Genuine, deduplicated Google Play Store reviews |
| **Store All-Time Rating** | **4.638★** | Cumulative historical score across 114k+ ratings |
| **Sample Mean Rating** | **3.707★** | Average rating within written review corpus |
| **Sample Median Rating** | **5.0★** | Polarized distribution (strong promoter base vs angry detractors) |
| **Positive Reviews (4-5★)** | **5,388 (67.35%)** | Commuters praising convenience, safety, and punctual rides |
| **Negative Reviews (1-2★)** | **2,369 (29.61%)** | Commuters experiencing operational or software friction |
| **Neutral Reviews (3★)** | **243 (3.04%)** | Mixed feedback or feature suggestions |
| **Date Range Covered** | **Dec 2023 – Oct 2026** | 34 months of longitudinal review telemetry |

---

## 3. Star Rating Distribution

| Star Rating | Review Count | Percentage Share | Cumulative Share | Visual Representation |
| :---: | :---: | :---: | :---: | :--- |
| **1★** | **2,094** | **26.17%** | 26.17% | `████████████████████` (26.2%) |
| **2★** | **275** | **3.44%** | 29.61% | `███` (3.4%) |
| **3★** | **243** | **3.04%** | 32.65% | `██` (3.0%) |
| **4★** | **654** | **8.18%** | 40.83% | `██████` (8.2%) |
| **5★** | **4,734** | **59.18%** | 100.00% | `████████████████████████████████████████` (59.2%) |
| **Total** | **8,000** | **100.00%** | — | — |

---

## 4. Empirical Complaint Theme Breakdown

Breakdown of specific complaint categories among negative reviews ($N_{neg} = 2,369$):

| Complaint Category | Negative Citations | % of Negative Reviews | Mean Rating | Community Upvotes | Priority |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **App Crashes & Performance** | **462** | **19.5%** | 1.90★ | 280 | **P1** |
| **GPS & Live Tracking Glitches** | **372** | **15.7%** | 2.62★ | **428** | **P0** |
| **Booking & Roster Flow** | **273** | **11.5%** | 2.39★ | 303 | **P1** |
| **Pickup Delays & Cab No-Show** | **252** | **10.6%** | 2.28★ | 263 | **P1** |
| **Login, SSO & Session Expiry** | **227** | **9.6%** | **1.47★** | 150 | **P1** |
| **Driver Conduct & Commute Safety** | **215** | **9.1%** | 2.77★ | 361 | **P2** |
| **OTP & Notification Friction** | **207** | **8.7%** | 1.90★ | 208 | **P0** |
| **Support Desk & Issue Resolution** | **139** | **5.9%** | 1.77★ | 115 | **P2** |
| **UI Usability & Forced Rating Prompts** | **131** | **5.5%** | 3.61★ | 236 | **P0** |
| **General Dissatisfaction (Venting)** | **768** | **32.4%** | 1.13★ | 333 | — |

*Note: Multi-label classification permits reviews to span multiple categories. Percentages sum to >100%.*

---

## 5. Top Upvoted Community Reviews

1. **Map Auto-Zoom Glitch (63 & 51 Upvotes)**  
   > *"One of the worst app. While tracking the cab in map. It's automatically zooming out after 3 4 seconds. Have to zoom in again. It's very frustrating!"* (1★, Jan 2024)
2. **Forced Rating Dialog Lockout (236 Upvotes across cluster)**  
   > *"forcing me to give rating after every ride, so I came here to give you 1 star. because if I don't rate, I can't use the app as there is no skip button."* (1★, Oct 2026)
3. **Boarding OTP Interception**  
   > *"The new feature and very annoying feature which you have introduced - when you click view otp , it pops up the seat belt safely first. Why do you ask for user input one more click . very annoying I should be able to see the otp in one click."* (2★, Oct 2026)
4. **App Crashes Post-Update (34 Upvotes)**  
   > *"The worst app I have ever seen. The app crashes frequently in first place. When try to make booking or update details it stops working... whenever i update this app, i need to uninstall and reinstall."* (1★, Mar 2024)
5. **ETA Calculation vs Traffic Reality**  
   > *"ETA calculator very bad. not sure on what basis its done. google maps always shows 3x the time shown in moveinsync app."* (1★, Oct 2026)

---

## 6. Prioritized Action Plan

* **P0 Hotfixes (Days 1–7)**:
  * Remove blocking seatbelt modal from "View OTP" action; render OTP chip persistently.
  * Disable map camera auto-reset on incoming GPS telemetry coordinates when user is interacting with map.
  * Add a clear "Skip" button to the post-ride in-app rating prompt.
* **P1 Platform Stability (Days 8–30)**:
  * Silent background OAuth2 token refresh to eliminate random logouts.
  * Crash-safe Room/SQLite migrations on app auto-update.
  * Traffic-aware dynamic ETA calibration with arrival confidence intervals.
  * Human-friendly booking shift terminology ("To Office" / "To Home").
* **P2 Strategic Operations (Days 31–90)**:
  * In-app transport desk live chat and dispatcher escalation bot.
  * Driver safety & AC compliance scorecard integration.

---

## 7. Rating-Monitoring & Refresh Workflow

To ensure Play Store ratings are monitored continually as requested in the case study brief, a repeatable automation workflow is implemented via:
* `python scripts/collect_reviews.py --target-count 5000`
* `python scripts/analyze_reviews.py`
* Running on a weekly GitHub Actions cron schedule with automated delta anomaly alerts when negative review share exceeds 25%.
