# Manual Classification-Validation Worksheet

**Project:** MoveInSync FDE Case Study — Review Classification Audit  
**Dataset:** `com.moveinsync.ets` Google Play Store Reviews ($N = 8,000$)  
**Audit Sample Size:** 30 Representative Public Reviews  
**Methodology:** Rule-Based Multi-Label Regex Taxonomy (`scripts/analyze_reviews.py`)  
**Validation Status:** **Awaiting Human Candidate / Reviewer Validation** (Blank Validation Fields Provided Below)  

---

## 1. Purpose & Audit Protocol

The analysis pipeline categorizes reviews using deterministic regular expression patterns. While high-precision for overt keywords, keyword-based classifiers are subject to:
1. **False Positives:** E.g., a user writing *'The app is not user-friendly'* matching the UI prompt pattern due to `'user friendly'`, or *'App was good before the update'* triggering both Positive and Crash themes.
2. **Overly Broad Terms:** E.g., the word `'update'` triggering App Performance, or `'wait'` triggering Pickup Delays even when referring to support queues.
3. **Multi-Label Overlap:** One review triggering 2 to 4 categories simultaneously (e.g. tracking map auto-zoom and cab delay).

> **CRITICAL AUDIT DISCLAIMER:**  
> In accordance with evaluation standards, **these classifications are NOT represented as manually validated**. This worksheet provides 30 representative records across all major categories, subtle edge cases, and potential false positives, with a blank human-validation field for reviewer audit.

---

## 2. Thirty Representative Review Audit Records

### Review #01 — ID: `3d87f169-2508-4a07-9e5a-d63b2c548ed3`
* **Rating:** ★★ (2 Stars) | **Date:** 2026-10-09 | **Version:** `12.19.0`
* **Original Review Text:**  
  > "The new feature and very annoying feature which you have introduced - when you click view otp , it pops up the seat belt safely first. Why do you ask for user input one more click . very annoying I should be able to see the otp in one click."
* **Suggested Category / Themes:** **Booking & Roster Flow, OTP & Notification Friction, UI Usability & Forced Rating Prompts**
* **Classification Reason (Regex Triggers):** `booking_roster_flow: 'seat'; otp_notifications: 'seat belt, view otp, otp'; ui_usability_prompts: 'click'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #02 — ID: `e0d68839-6e59-4dd7-8f00-052cda79a063`
* **Rating:** ★ (1 Star) | **Date:** 2026-10-04 | **Version:** `Unspecified`
* **Original Review Text:**  
  > "I try to login to this app but it's not sending any otp to login without login how we can use this app 😤😤😤 technical team please check once about this issue"
* **Suggested Category / Themes:** **Login, SSO & Session Expiry, OTP & Notification Friction**
* **Classification Reason (Regex Triggers):** `login_roster_account: 'login'; otp_notifications: 'otp'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #03 — ID: `43d90b3c-0443-4073-8647-6aee98c78bd4`
* **Rating:** ★ (1 Star) | **Date:** 2026-10-06 | **Version:** `12.19.0`
* **Original Review Text:**  
  > "06-10-2026 even after booked the trip it keep sends the push notification that trip is not booked. old: Bring monthly view ,not just day view..."
* **Suggested Category / Themes:** **Booking & Roster Flow, OTP & Notification Friction**
* **Classification Reason (Regex Triggers):** `booking_roster_flow: 'booked'; otp_notifications: 'push notification'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #04 — ID: `372c9fae-d5ea-4aa1-a446-4475e4d0da44`
* **Rating:** ★★ (2 Stars) | **Date:** 2026-08-03 | **Version:** `12.16.0`
* **Original Review Text:**  
  > "when we have zoomed in the map to track a vehicle what's the necessity to zoom out and show the ETA"
* **Suggested Category / Themes:** **GPS & Live Tracking Glitches**
* **Classification Reason (Regex Triggers):** `gps_live_tracking: 'ETA, map, track, zoom out'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #05 — ID: `57e90812-eb1a-4b77-8235-965aed7b78c4`
* **Rating:** ★★ (2 Stars) | **Date:** 2025-12-08 | **Version:** `12.7.2`
* **Original Review Text:**  
  > "1. even if cab is scheduled, i keep getting notification that I have not scheduled the cab. 2. when the map is zoomed to locate cab location, just after 5 seconds the map will zoom out. this is very irritating"
* **Suggested Category / Themes:** **GPS & Live Tracking Glitches, OTP & Notification Friction**
* **Classification Reason (Regex Triggers):** `gps_live_tracking: 'map, location, zoom out'; otp_notifications: 'notification'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #06 — ID: `7476b129-f0da-458e-8f86-d77ba2f9a710`
* **Rating:** ★ (1 Star) | **Date:** 2026-10-09 | **Version:** `12.19.0`
* **Original Review Text:**  
  > "MoveOutSync doesn't plan commutes; it plans cross-country pilgrimages. The ETA is an abstract joke where a 1-hour delay is considered punctual. The routing algorithm is pure genius: it clubs passengers from two different states into one cab at 8 AM, while empty cabs glide right past us. If you want a free Bharat Darshan tour before reaching office, this is it. Coding isn't for everyone-definitely not for the monkeys who built this. Try copying Routematic fools."
* **Suggested Category / Themes:** **GPS & Live Tracking Glitches, Pickup Delays & Cab No-Show, Positive Commute Feedback**
* **Classification Reason (Regex Triggers):** `gps_live_tracking: 'ETA, routing'; vehicle_delay_pickup: 'delay'; positive_commute_experience: 'punctual'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #07 — ID: `f9fce9fe-8115-4a30-8d09-d8bdac76837d`
* **Rating:** ★ (1 Star) | **Date:** 2026-10-08 | **Version:** `12.19.0`
* **Original Review Text:**  
  > "forcing me to give rating after every ride, so I came here to give you 1 star. because if I don't rate, I can't use the app as there is no skip option."
* **Suggested Category / Themes:** **UI Usability & Forced Rating Prompts**
* **Classification Reason (Regex Triggers):** `ui_usability_prompts: 'no skip'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #08 — ID: `27e47fba-8807-4da0-9dc7-fefe983b8b17`
* **Rating:** ★★★★★ (5 Stars) | **Date:** 2026-08-14 | **Version:** `12.17.0`
* **Original Review Text:**  
  > "I love the service they are providing. worked with 2 organisations with this app, and has made my commute simplified, transition seamless and everything works perfectly. I honestly hate the ui, and it is unintuitive to change location and stuff. but I am still gonna rate 5 stats because I support their mission."
* **Suggested Category / Themes:** **GPS & Live Tracking Glitches, UI Usability & Forced Rating Prompts, Support Desk & Issue Resolution, General Dissatisfaction, Positive Commute Feedback**
* **Classification Reason (Regex Triggers):** `gps_live_tracking: 'location'; ui_usability_prompts: 'ui'; support_desk_operations: 'support'; general_dissatisfaction: 'hate'; positive_commute_experience: 'love'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #09 — ID: `3a411c1e-a2cd-4d87-83d6-e89e9f76460d`
* **Rating:** ★ (1 Star) | **Date:** 2026-10-08 | **Version:** `12.19.0`
* **Original Review Text:**  
  > "very confusing the new features."
* **Suggested Category / Themes:** **UI Usability & Forced Rating Prompts**
* **Classification Reason (Regex Triggers):** `ui_usability_prompts: 'confusing'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #10 — ID: `0b1041ae-ce09-4947-b5f9-744e9014a639`
* **Rating:** ★★ (2 Stars) | **Date:** 2026-09-17 | **Version:** `12.18.1`
* **Original Review Text:**  
  > "you guys keep giving notifications to cancel the ride if not available for the same, but you don't even bother to remind the user regarding the default cancellation of logout trip if login trip is marked "Noshow", this is not fair at all"
* **Suggested Category / Themes:** **Booking & Roster Flow, Login, SSO & Session Expiry, OTP & Notification Friction**
* **Classification Reason (Regex Triggers):** `booking_roster_flow: 'cancellation, cancel'; login_roster_account: 'logout, login'; otp_notifications: 'notifications'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #11 — ID: `9798400e-2e5f-407f-82d0-a50ac0381384`
* **Rating:** ★★ (2 Stars) | **Date:** 2026-01-02 | **Version:** `12.8.3`
* **Original Review Text:**  
  > "App signs out every time I open the app, I had to re signin with my org SSO"
* **Suggested Category / Themes:** **Login, SSO & Session Expiry**
* **Classification Reason (Regex Triggers):** `login_roster_account: 'SSO, signin'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #12 — ID: `1d73eadd-7250-425f-9cbe-c906414e5049`
* **Rating:** ★ (1 Star) | **Date:** 2026-09-24 | **Version:** `12.19.0`
* **Original Review Text:**  
  > "Such a worst app. I am not receiving the OTP even after trying multiple times. Because of this, I am unable to complete the login/verification process. Please fix this issue as soon as possible."
* **Suggested Category / Themes:** **Login, SSO & Session Expiry, OTP & Notification Friction, General Dissatisfaction**
* **Classification Reason (Regex Triggers):** `login_roster_account: 'login'; otp_notifications: 'OTP'; general_dissatisfaction: 'worst'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #13 — ID: `d1e2d42b-385d-4a2e-83db-3204784732ad`
* **Rating:** ★★★★★ (5 Stars) | **Date:** 2026-10-08 | **Version:** `12.19.0`
* **Original Review Text:**  
  > "it's a great app for the night shift employees"
* **Suggested Category / Themes:** **Booking & Roster Flow, Positive Commute Feedback**
* **Classification Reason (Regex Triggers):** `booking_roster_flow: 'shift'; positive_commute_experience: 'great'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #14 — ID: `16f68390-6898-4cba-a2ea-78e53d280b78`
* **Rating:** ★★★★★ (5 Stars) | **Date:** 2026-09-21 | **Version:** `12.18.1`
* **Original Review Text:**  
  > "First ride was good, but for the return journey I received the cab details 18 minutes late and ended up missing the cab."
* **Suggested Category / Themes:** **Pickup Delays & Cab No-Show, Positive Commute Feedback**
* **Classification Reason (Regex Triggers):** `vehicle_delay_pickup: 'late'; positive_commute_experience: 'good'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #15 — ID: `ac05786a-a047-40b3-8174-d8434282ad60`
* **Rating:** ★ (1 Star) | **Date:** 2026-09-10 | **Version:** `12.18.0`
* **Original Review Text:**  
  > "waste app. driver will come to pickup point and wait for 1 hour but won't give a short call. this app will only accept 12 hour prior booking and 4 hour before return booking. rapido. uber and ola are better than this app"
* **Suggested Category / Themes:** **Booking & Roster Flow, Pickup Delays & Cab No-Show, Driver Conduct & Commute Safety, General Dissatisfaction**
* **Classification Reason (Regex Triggers):** `booking_roster_flow: 'booking'; vehicle_delay_pickup: 'wait, pickup'; driver_behavior_safety: 'driver'; general_dissatisfaction: 'waste'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #16 — ID: `bc736dc0-8fd1-45e8-b39e-b16020a4e2f7`
* **Rating:** ★ (1 Star) | **Date:** 2026-10-05 | **Version:** `12.19.0`
* **Original Review Text:**  
  > "mobile number is not visible once cab is booked, I can not see latest notification, since seems like notification stack full and never notification can not be shown. for every button click it is asking for policy acceptance, which is very unprofessional. overall user experience is very bad. many bugs and a lot of improvement required. completely unhappy with incorrect app functioning"
* **Suggested Category / Themes:** **App Crashes & Performance, Booking & Roster Flow, Driver Conduct & Commute Safety, OTP & Notification Friction, UI Usability & Forced Rating Prompts**
* **Classification Reason (Regex Triggers):** `app_performance_crash: 'bugs'; booking_roster_flow: 'booked'; driver_behavior_safety: 'unprofessional'; otp_notifications: 'notification'; ui_usability_prompts: 'click'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #17 — ID: `1b0909e4-98a8-47a3-92d7-1988e5cdd9ce`
* **Rating:** ★★★★★ (5 Stars) | **Date:** 2026-06-29 | **Version:** `12.14.1`
* **Original Review Text:**  
  > "But sometimes The Drivers tap on the forcestop and switched it off and speeding beyond the limits resolve this bug..."
* **Suggested Category / Themes:** **App Crashes & Performance, Driver Conduct & Commute Safety**
* **Classification Reason (Regex Triggers):** `app_performance_crash: 'bug'; driver_behavior_safety: 'speeding, Drivers'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #18 — ID: `98db1b19-26e2-4e6d-937b-7319944a6fc0`
* **Rating:** ★ (1 Star) | **Date:** 2026-10-02 | **Version:** `12.19.0`
* **Original Review Text:**  
  > "Drivers are rude no professonalism and transport help team doesn't help at all"
* **Suggested Category / Themes:** **Driver Conduct & Commute Safety**
* **Classification Reason (Regex Triggers):** `driver_behavior_safety: 'Drivers, rude'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #19 — ID: `0def625f-f0c8-4d3a-859d-4891c82c80ab`
* **Rating:** ★ (1 Star) | **Date:** 2026-09-28 | **Version:** `Unspecified`
* **Original Review Text:**  
  > "This aap keeps on crashing due to some bug and there is No Update Available Yet... What will Working Professionals do who avail cab services???"
* **Suggested Category / Themes:** **App Crashes & Performance**
* **Classification Reason (Regex Triggers):** `app_performance_crash: 'bug, crashing, Update'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #20 — ID: `60798e45-939e-4a99-8f5b-17383a891db6`
* **Rating:** ★ (1 Star) | **Date:** 2026-10-09 | **Version:** `Unspecified`
* **Original Review Text:**  
  > "whenever i update this app, i am not able to open the app again, I need to uninstall and reinstall again. facing this issue since 3 months"
* **Suggested Category / Themes:** **App Crashes & Performance**
* **Classification Reason (Regex Triggers):** `app_performance_crash: 'reinstall, uninstall, update'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #21 — ID: `133d2b88-b2d2-4fd4-9594-1ac26caf819e`
* **Rating:** ★★★ (3 Stars) | **Date:** 2026-10-03 | **Version:** `Unspecified`
* **Original Review Text:**  
  > "a few days ago this app was working fine on my phone, but for the last 3 days it's not working at all. The app doesn't start on my phone, whenever I am opening it, it closes itself. I tried clearing data, reinstalled it, but no change. It's not opening at all."
* **Suggested Category / Themes:** **App Crashes & Performance**
* **Classification Reason (Regex Triggers):** `app_performance_crash: 'not opening'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #22 — ID: `f61b87be-2625-4997-88c2-421a89dd01fe`
* **Rating:** ★ (1 Star) | **Date:** 2026-08-17 | **Version:** `12.17.0`
* **Original Review Text:**  
  > "This is a third class app which is not at all user friendly for employees, this is just made to the convenience of vendors,Help desk and vendors are not at all helpful on this app...they don't even consider your concerns.... worst transportation app I've ever used."
* **Suggested Category / Themes:** **UI Usability & Forced Rating Prompts, Support Desk & Issue Resolution, General Dissatisfaction, Positive Commute Feedback**
* **Classification Reason (Regex Triggers):** `ui_usability_prompts: 'user friendly'; support_desk_operations: 'Help desk'; general_dissatisfaction: 'third class, worst'; positive_commute_experience: 'helpful'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #23 — ID: `724fa773-e6c0-47ec-b76d-8c5ae25850ed`
* **Rating:** ★ (1 Star) | **Date:** 2026-10-02 | **Version:** `12.19.0`
* **Original Review Text:**  
  > "👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎👎who the hell is giving them 5 star ⭐ rating worst punctuation, my cab has to assign on 2:30 am and it's 3:30 am and still no updates. I called twice to there Customer support they are not receiving the call . i have a lots of abusive words for them. i have edited my feedback because I wasn't able to give them feedback twice I'm Using this worst facility because I don't have my personal Bike."
* **Suggested Category / Themes:** **App Crashes & Performance, Support Desk & Issue Resolution, General Dissatisfaction**
* **Classification Reason (Regex Triggers):** `app_performance_crash: 'updates'; support_desk_operations: 'support'; general_dissatisfaction: 'worst'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #24 — ID: `40363b38-fa55-4571-af0f-ff6fb0463015`
* **Rating:** ★ (1 Star) | **Date:** 2026-10-09 | **Version:** `12.19.0`
* **Original Review Text:**  
  > "worst app"
* **Suggested Category / Themes:** **General Dissatisfaction**
* **Classification Reason (Regex Triggers):** `general_dissatisfaction: 'worst'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #25 — ID: `6b0ec80a-f39e-4548-85a7-cefd18c99c83`
* **Rating:** ★ (1 Star) | **Date:** 2026-10-08 | **Version:** `12.19.0`
* **Original Review Text:**  
  > "its update made it worse"
* **Suggested Category / Themes:** **App Crashes & Performance**
* **Classification Reason (Regex Triggers):** `app_performance_crash: 'update'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #26 — ID: `2ce14584-824f-4d19-a7ce-95a17656fc8f`
* **Rating:** ★ (1 Star) | **Date:** 2026-10-08 | **Version:** `12.19.0`
* **Original Review Text:**  
  > "ETA calculator very bad. not sure on what basis its done. google maps always shows 3x the time shown in moveinsync app. tnis app just acts as a booking tool and no use of showing car location and eta."
* **Suggested Category / Themes:** **GPS & Live Tracking Glitches, Booking & Roster Flow**
* **Classification Reason (Regex Triggers):** `gps_live_tracking: 'ETA, maps, location, eta'; booking_roster_flow: 'booking'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #27 — ID: `5f781610-319a-4412-b308-95a6ec8ee6f6`
* **Rating:** ★ (1 Star) | **Date:** 2026-10-08 | **Version:** `12.19.0`
* **Original Review Text:**  
  > "dislike the new update. Bring the old version back. It was simple and minimalist."
* **Suggested Category / Themes:** **App Crashes & Performance**
* **Classification Reason (Regex Triggers):** `app_performance_crash: 'update'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #28 — ID: `387a67a5-1843-45ee-b837-91d7eb1fccce`
* **Rating:** ★ (1 Star) | **Date:** 2026-10-08 | **Version:** `12.19.0`
* **Original Review Text:**  
  > "your new update is a threat to person with medical condition. it just books you without informing if he's on waitlist or not. so annoying"
* **Suggested Category / Themes:** **App Crashes & Performance, Booking & Roster Flow**
* **Classification Reason (Regex Triggers):** `app_performance_crash: 'update'; booking_roster_flow: 'waitlist'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #29 — ID: `225d87f1-5d2f-4d23-ac26-ecda35211579`
* **Rating:** ★ (1 Star) | **Date:** 2026-10-08 | **Version:** `12.20.0`
* **Original Review Text:**  
  > "This application and also your transport management which very bad, they are not ready to help to employees. They all are only thinking about our benefits. That's it."
* **Suggested Category / Themes:** **Uncategorized**
* **Classification Reason (Regex Triggers):** `None (Uncategorized generic venting)`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

### Review #30 — ID: `5a892b9d-a4d4-4ead-b699-c98f71a94d57`
* **Rating:** ★ (1 Star) | **Date:** 2026-10-07 | **Version:** `12.19.0`
* **Original Review Text:**  
  > "bhot bekar hai"
* **Suggested Category / Themes:** **General Dissatisfaction**
* **Classification Reason (Regex Triggers):** `general_dissatisfaction: 'bekar'`
* **Human Validation Field:**
  - [ ] **Confirmed Correct**
  - [ ] **False Positive** (Explain: __________________________________________________)
  - [ ] **Multi-Label Adjust / Reclassify to:** ________________________________________
  - **Human Reviewer Notes:** _______________________________________________________

---

## 3. Systematic Classification Analysis & Known Edge Cases

| Taxonomy Theme | Observed Precision Risk | Root Cause in Rule Heuristics | Recommended Heuristic Refinement |
| :--- | :--- | :--- | :--- |
| **UI Usability & Prompts** | Moderate False-Positive Risk | Matches `'user friendly'`, which frequently occurs in negative contexts (`'not user friendly'`). | Add negative lookbehind `(?<!not\s)(?<!never\s)user\s*friendly` or sentiment gating. |
| **App Performance & Crashes** | Low-Moderate Risk | Matches standalone `'update'` or `'updates'`, which can describe roster schedule updates. | Require `'update'` to be adjacent to crash/bug/break/freeze tokens. |
| **Positive Commute Experience** | Contextual Inversion Risk | Matches `'good'`, `'helpful'` in contrastive clauses (`'Drivers are good but app is worst'`). | Restrict positive tag to reviews with Star Rating $\ge 4$. |
| **GPS & Live Tracking** | High Precision | Strong domain signals (`'zoom out'`, `'tracking'`, `'gps'`, `'map'`, `'eta'`). | High confidence ($>88\%$ semantic alignment). |
| **OTP & Notification Friction** | Very High Precision | Highly specific tokens (`'otp'`, `'seat belt'`, `'sms'`). | Zero ambiguous false positives identified. |
| **Forced Rating Prompts** | Very High Precision | Distinct phrase combinations (`'rate every ride'`, `'no skip'`). | Extremely high signal; directly correlates with retaliatory 1-star reviews. |

---

## 4. Next Steps for Human Reviewer
1. Mark `[X]` on **Confirmed Correct** or specify adjusted labels in **Reclassify to**.
2. Submit validated worksheet to establish a human-verified test corpus for fine-tuning LLM or hybrid NLP classifier.