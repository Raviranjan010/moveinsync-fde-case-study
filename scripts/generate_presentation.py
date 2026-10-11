"""
MoveInSync FDE Case Study - Executive Presentation Generator
Author: Forward Deployed Engineer (FDE) Candidate
Output: reports/MoveInSync_Case_Study_Presentation.pptx
"""

import os
import sys
import json
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# Brand Palette
DARK_NAVY = RGBColor(29, 53, 87)       # #1d3557
STEEL_BLUE = RGBColor(69, 123, 157)    # #457b9d
CORAL_RED = RGBColor(230, 57, 70)      # #e63946
BG_LIGHT = RGBColor(248, 250, 252)     # #f8fafc
WHITE = RGBColor(255, 255, 255)
TEXT_DARK = RGBColor(15, 23, 42)       # #0f172a
TEXT_MUTED = RGBColor(100, 116, 139)   # #64748b
BORDER_COLOR = RGBColor(226, 232, 240)


def create_deck(
    metrics_path: str = "data/processed/analysis_metrics.json",
    meta_path: str = "data/raw/collection_metadata.json",
    figures_dir: str = "reports/figures",
    output_pptx: str = "reports/MoveInSync_Case_Study_Presentation.pptx"
):
    prs = Presentation()
    prs.slide_width = Inches(13.333)  # 16:9 standard widescreen
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]

    # Load metrics
    with open(metrics_path, "r", encoding="utf-8") as f:
        metrics = json.load(f)

    def add_header(slide, title_text, category_text="MOVEINSYNC | FORWARD DEPLOYED ENGINEER CASE STUDY"):
        # Category header
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(9.5)
        p_cat.font.bold = True
        p_cat.font.color.rgb = STEEL_BLUE

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = DARK_NAVY

    # ================= SLIDE 1: TITLE SLIDE =================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = DARK_NAVY
    bg1.line.color.rgb = DARK_NAVY

    tb1 = s1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(10.9), Inches(3.8))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "MoveInSync | Play Store Rating Intelligence"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = WHITE

    p2 = tf1.add_paragraph()
    p2.text = "Empirical Review Diagnostics, Baseline Reconciliation & Prioritized Engineering Action Plan"
    p2.font.size = Pt(18)
    p2.font.color.rgb = RGBColor(168, 218, 220)
    p2.space_before = Pt(12)

    p3 = tf1.add_paragraph()
    p3.text = "Target App: MoveInSync (com.moveinsync.ets) | Dataset: N = 8,000 Genuine Verified Reviews\nCandidate: Forward Deployed Engineer (Intern to FTE) | Date: October 2026"
    p3.font.size = Pt(12)
    p3.font.color.rgb = RGBColor(226, 232, 240)
    p3.space_before = Pt(32)

    # ================= SLIDE 2: STOREFRONT BASELINE RECONCILIATION =================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Rating Baseline Reconciliation: Storefront vs Sample Reality")

    # Card 1: India Storefront
    c1 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(3.6), Inches(5.2))
    c1.fill.solid()
    c1.fill.fore_color.rgb = BG_LIGHT
    c1.line.color.rgb = BORDER_COLOR
    tf_c1 = c1.text_frame
    tf_c1.word_wrap = True
    p = tf_c1.paragraphs[0]
    p.text = "India Storefront (gl=IN)\nPrimary Market (>99% Rides)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = STEEL_BLUE

    p = tf_c1.add_paragraph()
    p.text = "4.64 ★"
    p.font.size = Pt(38)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_before = Pt(8)

    p = tf_c1.add_paragraph()
    p.text = "• Total Store Ratings: 114,867\n• Total Store Reviews: 23,619\n• Total Installs: 1,000,000+\n• Official Active Version: 12.19.0\n\nAggregates 1-tap silent star ratings from employees across 430+ enterprise accounts over multiple years."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.space_before = Pt(12)

    # Card 2: US Storefront
    c2 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.8), Inches(1.6), Inches(3.6), Inches(5.2))
    c2.fill.solid()
    c2.fill.fore_color.rgb = BG_LIGHT
    c2.line.color.rgb = BORDER_COLOR
    tf_c2 = c2.text_frame
    tf_c2.word_wrap = True
    p = tf_c2.paragraphs[0]
    p.text = "US Storefront (gl=US)\nReviewer Snapshot"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = STEEL_BLUE

    p = tf_c2.add_paragraph()
    p.text = "4.32 ★"
    p.font.size = Pt(38)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p.space_before = Pt(8)

    p = tf_c2.add_paragraph()
    p.text = "• Discrepancy Resolved:\n  Google Play localizes displayed ratings by device registration and country (policy since late 2021).\n• US Storefront Sample: 100 reviews\n• Partner Lite App: 4.25★ (~4.3★)\n\nExplains why external evaluators saw ~4.3★ while India users see 4.64★."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.space_before = Pt(12)

    # Card 3: Written Review Sample
    c3 = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.2))
    c3.fill.solid()
    c3.fill.fore_color.rgb = BG_LIGHT
    c3.line.color.rgb = BORDER_COLOR
    tf_c3 = c3.text_frame
    tf_c3.word_wrap = True
    p = tf_c3.paragraphs[0]
    p.text = "Written Review Sample\nEmpirical Corpus (N = 8,000)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = CORAL_RED

    p = tf_c3.add_paragraph()
    p.text = "3.71 ★"
    p.font.size = Pt(38)
    p.font.bold = True
    p.font.color.rgb = CORAL_RED
    p.space_before = Pt(8)

    p = tf_c3.add_paragraph()
    p.text = "• Negative Reviews (1-2★): 2,369 (29.61%)\n• Positive Reviews (4-5★): 5,388 (67.35%)\n• Neutral Reviews (3★): 243 (3.04%)\n\nNegative Selection Bias: Riders encountering curbside failures actively write text reviews, while satisfied riders give silent 5-star ratings."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.space_before = Pt(12)

    # ================= SLIDE 3: DATA AUDIT & VERIFICATION =================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Dataset Verification Audit: 100% Genuine Provenance Confirmed")

    tb_v = s3.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(6.0), Inches(5.2))
    tf_v = tb_v.text_frame
    tf_v.word_wrap = True
    p = tf_v.paragraphs[0]
    p.text = "Verification Audit Methodology & Findings"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY

    findings = [
        ("Observation Addressed", "Existing review IDs appear UUID-like rather than base64 strings."),
        ("Controlled Verification Test", "Fresh collection of 100 live reviews into data/verification/ executed on Oct 11, 2026."),
        ("Empirical Congruence Result", "100 out of 100 verification reviews matched the existing dataset with 100% field congruence."),
        ("UUID Format Provenance", "Confirmed that Google Play's internal API returns UUID v4 strings natively for com.moveinsync.ets reviews."),
        ("Zero Fabrication Guarantee", "All 8,000 records are authentic public Google Play reviews collected via google-play-scraper."),
        ("User Privacy Protection", "Reviewer display names (user_name) redacted to [REDACTED] in public repo files.")
    ]
    for title, desc in findings:
        p = tf_v.add_paragraph()
        p.text = f"• {title}: {desc}"
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)

    # Insert Figure 1 on the right
    fig1 = os.path.join(figures_dir, "figure1_rating_distribution.png")
    if os.path.exists(fig1):
        s3.shapes.add_picture(fig1, Inches(7.1), Inches(1.8), width=Inches(5.4))

    # ================= SLIDE 4: COMPLAINT THEMES & DENOMINATORS =================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Empirical Complaint Categories & Multi-Label Breakdown")

    fig3 = os.path.join(figures_dir, "figure3_complaint_themes_frequency.png")
    if os.path.exists(fig3):
        s4.shapes.add_picture(fig3, Inches(0.8), Inches(1.6), width=Inches(6.2))

    tb_theme = s4.shapes.add_textbox(Inches(7.3), Inches(1.6), Inches(5.2), Inches(5.2))
    tf_theme = tb_theme.text_frame
    tf_theme.word_wrap = True
    p = tf_theme.paragraphs[0]
    p.text = "Multi-Label Taxonomy & Denominator Rules"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY

    theme_notes = [
        "Denominator Standards: Total Sample N = 8,000; Negative Subset N_neg = 2,369 (29.61%).",
        "Multi-Label Classification: One review can match multiple themes (e.g. Map Zoom Out AND Delay). Sum of theme percentages exceeds 100% (specifically 262.1% across negative reviews).",
        "#1 Operational Glitch: GPS & Live Tracking (372 neg reviews, 15.7% of N_neg, 428 upvotes).",
        "#2 Platform Stability: Crashes & Update Errors (462 neg reviews, 19.5% of N_neg, 280 upvotes).",
        "#3 Booking / Shift Confusion: Roster Flow (273 neg reviews, 11.5% of N_neg, 303 upvotes).",
        "#4 Commute Punctuality: Vehicle Delays (252 neg reviews, 10.6% of N_neg, 263 upvotes).",
        "#5 Curbside Boarding: OTP Friction (207 neg reviews, 8.7% of N_neg, 208 upvotes)."
    ]
    for note in theme_notes:
        p = tf_theme.add_paragraph()
        p.text = f"• {note}"
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(8)

    # ================= SLIDE 5: P0 HOTFIX - OTP & SAFETY MODAL =================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "P0 Hotfix: Boarding OTP Delay & Seatbelt Modal Decoupling", "RECOMMENDATION REC-01 | IMMEDIATE SPRINT 1 HOTFIX")

    col_l = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
    col_l.fill.solid()
    col_l.fill.fore_color.rgb = BG_LIGHT
    col_l.line.color.rgb = BORDER_COLOR
    tf_l = col_l.text_frame
    tf_l.word_wrap = True
    p = tf_l.paragraphs[0]
    p.text = "Verified User Problem & Evidence"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = CORAL_RED

    p = tf_l.add_paragraph()
    p.text = "• Problem: Tapping 'View OTP' displays a blocking modal dialog requiring rider to confirm seatbelt safety before revealing the OTP.\n• Curbside Impact: Drivers refuse to unlock doors without OTP; employees in hurried morning lines experience curbside delays, vehicle queues, and driver arguments.\n• Evidence: 207 / 2,369 negative reviews (8.7%), 208 upvotes, mean rating 1.90★.\n\nUser Quote:\n'The new feature and very annoying feature which you have introduced - when you click view otp , it pops up the seat belt safely first. Why do you ask for user input one more click . very annoying I should be able to see the otp in one click.'"
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.space_before = Pt(8)

    col_r = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2))
    col_r.fill.solid()
    col_r.fill.fore_color.rgb = BG_LIGHT
    col_r.line.color.rgb = BORDER_COLOR
    tf_r = col_r.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "Technical Solution & Governance"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = STEEL_BLUE

    p = tf_r.add_paragraph()
    p.text = "1. Persistent OTP Header Chip:\n   Render 4-digit boarding OTP persistently in large bold font on trip card header without requiring a button click.\n2. Decouple Seatbelt Awareness:\n   Replace blocking modal with a passive, animated post-boarding banner informing riders to fasten seatbelt once trip starts.\n3. Safety Compliance Protected:\n   Retains corporate legal/safety mandate while eliminating interactive boarding roadblock.\n\n• Responsible Squad: Mobile App Squad & UX Design\n• Observable Metric: Time to display OTP (<0.5s); curbside dispute rate.\n• Experiment: 50/50 A/B test on 2 client sites."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.space_before = Pt(8)

    # ================= SLIDE 6: P0 HOTFIX - MAP AUTO-ZOOM =================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "P0 Hotfix: Map Auto-Zoom Camera Reset Bug During Live Tracking", "RECOMMENDATION REC-02 | IMMEDIATE SPRINT 1 HOTFIX")

    col_l = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
    col_l.fill.solid()
    col_l.fill.fore_color.rgb = BG_LIGHT
    col_l.line.color.rgb = BORDER_COLOR
    tf_l = col_l.text_frame
    tf_l.word_wrap = True
    p = tf_l.paragraphs[0]
    p.text = "Verified User Problem & Evidence"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = CORAL_RED

    p = tf_l.add_paragraph()
    p.text = "• Problem: While tracking approaching cab, map view automatically resets camera zoom and re-centers every 3-4 seconds, overriding user pinch-to-zoom gestures.\n• User Impact: Riders cannot inspect vehicle street location or whether driver is stuck at an intersection; complete tracking breakdown.\n• Evidence: 372 / 2,369 negative reviews (15.7%), 428 upvotes (highest community upvotes in entire dataset).\n\nUser Quotes:\n'While tracking the cab in map. It's automatically zooming out after 3 4 seconds. Have to zoom in again. It's very frustrating!' (51 upvotes)\n'No matter how many times the user zoom in to see the cab location, the app is designed to zoom out in 2 seconds!' (19 upvotes)"
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.space_before = Pt(8)

    col_r = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2))
    col_r.fill.solid()
    col_r.fill.fore_color.rgb = BG_LIGHT
    col_r.line.color.rgb = BORDER_COLOR
    tf_r = col_r.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "Technical Solution & Governance"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = STEEL_BLUE

    p = tf_r.add_paragraph()
    p.text = "1. Decouple Marker from Camera:\n   Incoming GPS coordinate updates update vehicle marker position (cabMarker.setPosition()) without invoking map.animateCamera().\n2. User Gesture Listener Flag:\n   Maintain isUserInteracting flag. Suppress automated bounding box animations while user is inspecting map.\n3. Explicit 'Re-Center on Cab' FAB:\n   Provide a Floating Action Button allowing user to snap back to vehicle view when desired.\n\n• Responsible Squad: Mobile Maps SDK Squad\n• Observable Metric: Camera auto-reset interrupts per session; map gesture retention time.\n• Validation: Beta rollout with instrumentation on camera animation override events."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.space_before = Pt(8)

    # ================= SLIDE 7: P0 HOTFIX - FORCED RATING PROMPTS =================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "P0 Hotfix: Make Post-Ride Rating Prompts Optional & Dismissible", "RECOMMENDATION REC-03 | IMMEDIATE SPRINT 1 HOTFIX")

    col_l = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
    col_l.fill.solid()
    col_l.fill.fore_color.rgb = BG_LIGHT
    col_l.line.color.rgb = BORDER_COLOR
    tf_l = col_l.text_frame
    tf_l.word_wrap = True
    p = tf_l.paragraphs[0]
    p.text = "Verified User Problem & Evidence"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = CORAL_RED

    p = tf_l.add_paragraph()
    p.text = "• Problem: Upon app relaunch, riders are blocked by a full-screen unskippable modal demanding rating for their previous trip.\n• Retaliatory Feedback Loop: Users in a hurry to book next shift or check schedule are locked out, prompting them to open Google Play Store and retaliate with 1-star reviews.\n• Evidence: 131 / 2,369 negative reviews (5.5%), 236 community upvotes.\n\nUser Quote:\n'forcing me to give rating after every ride, so I came here to give you 1 star. because if I don't rate, I can't use the app as there is no skip button.'"
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.space_before = Pt(8)

    col_r = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2))
    col_r.fill.solid()
    col_r.fill.fore_color.rgb = BG_LIGHT
    col_r.line.color.rgb = BORDER_COLOR
    tf_r = col_r.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "Technical Solution & Governance"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = STEEL_BLUE

    p = tf_r.add_paragraph()
    p.text = "1. Explicit 'Skip / Dismiss' Action:\n   Add an unambiguous, prominent Skip button on all post-trip feedback cards.\n2. Non-Intrusive Bottom Sheet:\n   Convert blocking modal into an unobtrusive bottom-sheet card that auto-collapses after 10 seconds of inactivity.\n3. Vendor SLA Protection:\n   Operations continues to collect ratings from willing passengers without creating punitive app lockouts.\n\n• Responsible Squad: Product Design & Mobile Squad\n• Observable Metric: In-app feedback dismissal rate vs submission rate; 30-day Play Store 1-star review velocity.\n• Validation: A/B rollout across 25% tenant fleet."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.space_before = Pt(8)

    # ================= SLIDE 8: P1 PLATFORM RELIABILITY & ROSTER CLARITY =================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "P1 Enhancements: Session Resilience, Traffic ETA & Roster Clarity", "RECOMMENDATIONS REC-04, REC-05, REC-06 | 30-DAY WINDOW")

    # REC-04
    c_r4 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(3.6), Inches(5.2))
    c_r4.fill.solid()
    c_r4.fill.fore_color.rgb = BG_LIGHT
    c_r4.line.color.rgb = BORDER_COLOR
    tf = c_r4.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "REC-04: Session Auth & Stability\n(227 neg rev / 9.6%, 1.47★)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p = tf.add_paragraph()
    p.text = "• Problem: Frequent involuntary logouts and post-update app crashes forcing uninstalls.\n• Solution: Silent OAuth2 refresh token background worker using Android Keystore. Intercept 401 HTTP errors to renew tokens silently before routing to login. Add crash-safe Room database migration tests.\n• Metric: Daily involuntary logout rate (<1.0%); Crashlytics crash-free sessions (>99.5%)."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_DARK
    p.space_before = Pt(8)

    # REC-05
    c_r5 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.8), Inches(1.6), Inches(3.6), Inches(5.2))
    c_r5.fill.solid()
    c_r5.fill.fore_color.rgb = BG_LIGHT
    c_r5.line.color.rgb = BORDER_COLOR
    tf = c_r5.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "REC-05: Traffic-Aware ETA\n(252 neg rev / 10.6%, 263 up)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p = tf.add_paragraph()
    p.text = "• Problem: Static distance-based ETA underestimates city traffic (e.g. MoveInSync 10m vs Google Maps 35m).\n• Solution: Ingest live traffic layer matrices. Display arrival confidence intervals ('14–18 min (Heavy Traffic)') rather than single optimistic points. Trigger auto-alert if cab delayed >10 min.\n• Metric: ETA Mean Absolute Error (MAE <= 5 min); delay support ticket volume."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_DARK
    p.space_before = Pt(8)

    # REC-06
    c_r6 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.8), Inches(1.6), Inches(3.7), Inches(5.2))
    c_r6.fill.solid()
    c_r6.fill.fore_color.rgb = BG_LIGHT
    c_r6.line.color.rgb = BORDER_COLOR
    tf = c_r6.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "REC-06: Roster Terminology\n(273 neg rev / 11.5%, 303 up)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY
    p = tf.add_paragraph()
    p.text = "• Problem: Industry terms 'Login/Logout' shift commutes confused with app authentication, causing reverse-direction bookings.\n• Solution: Revamp copy to intuitive labels: 'To Office (Pickup)' and 'To Home (Drop)'. Display prominent cutoff countdown badges ('Booking closes in 45 min').\n• Metric: Self-booking funnel completion rate; reverse-booking support ticket rate."
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_DARK
    p.space_before = Pt(8)

    # ================= SLIDE 9: PRIORITIZED RECOMMENDATION ROADMAP =================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Prioritized Recommendation Matrix & Sprint Roadmap")

    # Add Table
    rows = 9
    cols = 6
    top = Inches(1.6)
    left = Inches(0.8)
    width = Inches(11.7)
    height = Inches(5.2)

    table_shape = s9.shapes.add_table(rows, cols, left, top, width, height)
    tbl = table_shape.table

    headers = ["ID", "Pri", "Theme", "Key Recommended Action", "Responsible Squad", "Primary Metric"]
    col_widths = [Inches(0.9), Inches(0.7), Inches(2.2), Inches(4.3), Inches(2.0), Inches(1.6)]
    for i, w in enumerate(col_widths):
        tbl.columns[i].width = w

    for i, h in enumerate(headers):
        cell = tbl.cell(0, i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = DARK_NAVY
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = WHITE

    table_data = [
        ("REC-01", "P0", "OTP Friction", "Persistent OTP banner; decouple seatbelt popup into non-blocking animation.", "Mobile & UX", "OTP view time <0.5s"),
        ("REC-02", "P0", "GPS Tracking", "Decouple cab marker updates from camera bounding animation; add re-center FAB.", "Maps SDK Squad", "Auto-reset interrupts = 0"),
        ("REC-03", "P0", "Rating Prompts", "Add prominent Skip button on ride rating card; auto-dismiss on inactivity.", "Product Design", "Retaliatory 1★ velocity"),
        ("REC-04", "P1", "Session / Auth", "Silent background OAuth2 token refresh worker; crash-safe DB migrations.", "Mobile Platform", "Involuntary logout <1%"),
        ("REC-05", "P1", "ETA Accuracy", "Dynamic traffic layer integration; display arrival confidence windows.", "Routing Algorithms", "ETA MAE <= 5 min"),
        ("REC-06", "P1", "Booking Flow", "Human-centered copy ('To Office'/'To Home'); cutoff countdown timers.", "Product Design", "Booking funnel drop-off"),
        ("REC-07", "P2", "Support Desk", "In-app issue bot with 1-tap quick actions and live client marshal escalation.", "FDE & Ops Tech", "First Response <2 min"),
        ("REC-08", "P2", "Driver Safety", "Post-ride AC feedback chips; driver telematics speed monitoring loop.", "Driver Ecosystem", "Overspeed / 1,000 km")
    ]

    for row_idx, r_data in enumerate(table_data, 1):
        for col_idx, text in enumerate(r_data):
            cell = tbl.cell(row_idx, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = BG_LIGHT if row_idx % 2 == 1 else WHITE
            p = cell.text_frame.paragraphs[0]
            p.text = text
            p.font.size = Pt(9.5)
            if col_idx == 1 and text == "P0":
                p.font.bold = True
                p.font.color.rgb = CORAL_RED
            else:
                p.font.color.rgb = TEXT_DARK

    # ================= SLIDE 10: MONITORING, LIMITATIONS & AI METHODOLOGY =================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Repeatable Monitoring, Telemetry Boundaries & Methodology Disclosure")

    col_l = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.2))
    col_l.fill.solid()
    col_l.fill.fore_color.rgb = BG_LIGHT
    col_l.line.color.rgb = BORDER_COLOR
    tf_l = col_l.text_frame
    tf_l.word_wrap = True
    p = tf_l.paragraphs[0]
    p.text = "Repeatable Monitoring & Telemetry Boundaries"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = DARK_NAVY

    p = tf_l.add_paragraph()
    p.text = "• Answering 'How are our ratings?':\n  Repeatable CLI pipeline: scripts/collect_reviews.py, scripts/analyze_reviews.py, and scripts/refresh_monitoring.py refresh dataset and metrics deterministically.\n• Automated GitHub Action (.github/workflows/monitor_ratings.yml) provides weekly cron scheduling (presented as locally tested / proposed workflow).\n• Operational Alerting: Console threshold alerting active; webhook dispatch supported via ALERT_WEBHOOK_URL.\n• Telemetry Boundaries:\n  Public Play Store reviews represent user experience symptoms. Underlying technical root causes are engineering hypotheses requiring internal Crashlytics and Datadog validation."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.space_before = Pt(8)

    col_r = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.2))
    col_r.fill.solid()
    col_r.fill.fore_color.rgb = BG_LIGHT
    col_r.line.color.rgb = BORDER_COLOR
    tf_r = col_r.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "Tooling, Stack & AI Assistance Disclosure"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = STEEL_BLUE

    p = tf_r.add_paragraph()
    p.text = "• Core Technology Stack:\n  Python 3.12, google-play-scraper (v1.2.7), pandas (v3.0.5), matplotlib (v3.11.2), seaborn (v0.13.2), reportlab (v5.0.1), python-pptx (v1.0.2), streamlit (v1.63.0), pytest (v9.1.1).\n• Permitted AI Assistance Disclosure:\n  In compliance with assignment terms ('Use any tools you like, AI included'): AI coding assistants were utilized for exploratory regex structuring, test generation, and slide compilation scripts.\n• Independent Human Verification:\n  All data verification comparisons, mathematical aggregations, and recommendations were verified through deterministic code and documented worksheets."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_DARK
    p.space_before = Pt(8)

    prs.save(output_pptx)
    print(f"[+] Successfully compiled executive presentation to: {output_pptx}")


if __name__ == "__main__":
    create_deck()
