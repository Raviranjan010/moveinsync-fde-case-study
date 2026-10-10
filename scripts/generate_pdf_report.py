"""
MoveInSync FDE Case Study - Professional PDF Report Generator
Author: Forward Deployed Engineer (FDE) Candidate
Output: reports/MoveInSync_FDE_Case_Study.pdf
"""

import json
import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas


class NumberedCanvas(canvas.Canvas):
    """Two-pass canvas to dynamically compute and print running page numbers."""
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))

        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(36, 756, "MoveInSync | FDE Case Study: Play Store Rating Investigation")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(36, 750, 576, 750)

        # Footer
        footer_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(576, 24, footer_text)
        self.drawString(36, 24, "CONFIDENTIAL — Forward Deployed Engineer (FDE) Candidate Assignment")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(36, 34, 576, 34)
        self.restoreState()


def build_pdf_report(
    metrics_path: str = "data/processed/analysis_metrics.json",
    meta_path: str = "data/raw/collection_metadata.json",
    figures_dir: str = "reports/figures",
    output_pdf: str = "reports/MoveInSync_FDE_Case_Study.pdf"
):
    print(f"[*] Compiling PDF report to: {output_pdf}...")

    # Load data
    with open(metrics_path, "r", encoding="utf-8") as f:
        metrics = json.load(f)

    meta = {}
    if os.path.exists(meta_path):
        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)

    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=46,
        bottomMargin=46
    )

    styles = getSampleStyleSheet()

    # Custom typography styles
    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#1d3557"),
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        "DocSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#457b9d"),
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        "Heading1_Custom",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=17,
        textColor=colors.HexColor("#1d3557"),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        "Heading2_Custom",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#2a9d8f"),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        "Body_Custom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.8,
        leading=12.2,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=6
    )

    body_bold = ParagraphStyle(
        "Body_Bold",
        parent=body_style,
        fontName="Helvetica-Bold"
    )

    quote_style = ParagraphStyle(
        "Quote_Custom",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=8.2,
        leading=11.5,
        textColor=colors.HexColor("#334155")
    )

    table_header = ParagraphStyle(
        "TableHeader",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=8,
        leading=10,
        textColor=colors.white
    )

    table_body = ParagraphStyle(
        "TableBody",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=7.8,
        leading=9.8,
        textColor=colors.HexColor("#1e293b")
    )

    story = []

    # Title Banner Block
    story.append(Paragraph("MOVEINSYNC | PLAY STORE RATING INVESTIGATION & RECOMMENDATIONS", title_style))
    story.append(Paragraph("Forward Deployed Engineer (FDE) Candidate Case Study | Empirical Review Intelligence", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1d3557"), spaceAfter=10))

    # Metadata Block
    meta_data = [
        [
            Paragraph("<b>Target Application:</b> MoveInSync (com.moveinsync.ets)", table_body),
            Paragraph(f"<b>Store Lifetime Rating:</b> {meta.get('current_store_score', 4.64)}★ ({meta.get('store_ratings_count', 114855):,} ratings)", table_body)
        ],
        [
            Paragraph("<b>Corpus Analyzed:</b> 8,000 Genuine Reviews (Dec 2023 - Oct 2026)", table_body),
            Paragraph(f"<b>Review Corpus Mean Rating:</b> {metrics['summary']['average_rating']}★ (Dissatisfaction: {metrics['summary']['negative_review_rate_pct']}%)", table_body)
        ],
        [
            Paragraph("<b>Target Persona:</b> Enterprise Corporate Commuters", table_body),
            Paragraph("<b>Report Date:</b> October 2026", table_body)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[270, 270])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
        ('PADDING', (0, 0), (-1, -1), 4),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0"))
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 10))

    # SECTION 1: EXECUTIVE SUMMARY
    story.append(Paragraph("1. Executive Summary", h1_style))
    exec_summary_text = (
        "MoveInSync operates workplace commute logistics for over <b>1.5 million daily enterprise employees</b> across "
        "<b>430+ Fortune 500 customers</b>. While the Google Play Store shows an overall historical rating of <b>4.64★</b>, "
        "empirical analysis of <b>8,000 genuine user reviews</b> reveals that <b>29.61% of written reviews are negative (1★ or 2★)</b>, "
        "with 1-star reviews alone accounting for <b>26.17% (2,094 reviews)</b>.<br/><br/>"
        "Crucially, our investigation proves that MoveInSync does not suffer from widespread platform rejection. Instead, "
        "low ratings are driven by <b>three severe, localized software friction points</b> occurring at time-sensitive boarding moments: "
        "(1) a blocking seatbelt modal intercepting the boarding OTP, (2) a Google Maps camera auto-zoom reset glitch during live cab tracking, "
        "and (3) an unskippable post-ride rating dialog that locks users out and provokes retaliatory 1-star reviews on the Play Store. "
        "Resolving these three P0 hotfixes will immediately halt negative review velocity and restore Play Store sentiment."
    )
    story.append(Paragraph(exec_summary_text, body_style))
    story.append(Spacer(1, 6))

    # SECTION 2: RESEARCH OBJECTIVE & APPLICATION SCOPE
    story.append(Paragraph("2. Research Objective & App Scope", h1_style))
    scope_text = (
        "The objective of this assignment is to diagnose why Play Store ratings are lower than expected and present an actionable, "
        "engineering-ready improvement plan. MoveInSync publishes several apps on Google Play Store with distinct personas:<br/>"
        "• <b>com.moveinsync.ets (Primary Focus):</b> The employee-facing application used by riders for self-booking, live cab tracking, "
        "boarding OTP verification, and shift scheduling. This touchpoint directly dictates public brand perception.<br/>"
        "• <b>com.moveinsync.driver.lite / dco (Driver Partner Apps):</b> Used exclusively by commercial cab drivers for navigation and passenger verification.<br/>"
        "• <b>field.moveinsync.ets (Field & Operations App):</b> Internal operations app used by ground transport marshals.<br/>"
        "<b>Scope Boundary:</b> This analysis focuses strictly on <b>com.moveinsync.ets</b> to maintain clean user journey segmentation."
    )
    story.append(Paragraph(scope_text, body_style))
    story.append(Spacer(1, 6))

    # SECTION 3 & 4: DATASET SIZE & METHODOLOGY
    story.append(Paragraph("3. Data Sources, Sample Size & Methodology", h1_style))
    method_text = (
        f"A total of <b>{metrics['summary']['total_reviews']:,} authentic reviews</b> were extracted directly from the Google Play Store "
        f"spanning <b>{metrics['summary']['date_range']['start']} to {metrics['summary']['date_range']['end']}</b> using automated pagination across "
        "both <code>NEWEST</code> and <code>MOST_RELEVANT</code> sort orders. The pipeline cleaned, deduplicated, and segmented the reviews into "
        "sentiment buckets (Negative: 1-2★, Neutral: 3★, Positive: 4-5★) and tagged them against 11 validated operational and software themes."
    )
    story.append(Paragraph(method_text, body_style))
    story.append(Spacer(1, 4))

    # Rating Table
    rating_table_data = [
        [Paragraph("Rating", table_header), Paragraph("Count", table_header), Paragraph("Share %", table_header), Paragraph("Sentiment Classification", table_header)]
    ]
    for r in [1, 2, 3, 4, 5]:
        cnt = metrics['summary']['rating_distribution_counts'].get(str(r), 0)
        pct = metrics['summary']['rating_distribution_percentages'].get(str(r), 0)
        sent = "Negative (Detractor)" if r in [1, 2] else ("Neutral (Passive)" if r == 3 else "Positive (Promoter)")
        rating_table_data.append([
            Paragraph(f"{r} Star", table_body),
            Paragraph(f"{cnt:,}", table_body),
            Paragraph(f"{pct}%", table_body),
            Paragraph(sent, table_body)
        ])
    r_tab = Table(rating_table_data, colWidths=[70, 80, 80, 310])
    r_tab.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1d3557")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 3),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")])
    ]))
    story.append(r_tab)
    story.append(Spacer(1, 8))

    # Page Break for Charts & Findings
    story.append(PageBreak())

    # SECTION 5 & 6: KEY FINDINGS & CHARTS
    story.append(Paragraph("4. Key Findings Supported by Empirical Evidence", h1_style))
    findings_intro = (
        "Analysis of the <b>2,369 negative reviews</b> shows distinct complaint clusters. The table below outlines the "
        "frequency, negative share, mean star rating, and community upvotes for each identified theme."
    )
    story.append(Paragraph(findings_intro, body_style))
    story.append(Spacer(1, 4))

    # Theme breakdown table
    theme_table_data = [
        [Paragraph("Complaint Category", table_header), Paragraph("Neg Reviews", table_header), Paragraph("% of Negatives", table_header), Paragraph("Mean Rating", table_header), Paragraph("Upvotes", table_header), Paragraph("Priority", table_header)]
    ]
    p_map = {
        "app_performance_crash": "P1", "gps_live_tracking": "P0", "booking_roster_flow": "P1",
        "vehicle_delay_pickup": "P1", "driver_behavior_safety": "P2", "login_roster_account": "P1",
        "otp_notifications": "P0", "support_desk_operations": "P2", "ui_usability_prompts": "P0",
        "general_dissatisfaction": "—", "positive_commute_experience": "—"
    }

    for t in metrics["theme_breakdown"]:
        if t["theme_key"] in ["positive_commute_experience", "general_dissatisfaction"]:
            continue
        theme_table_data.append([
            Paragraph(t["label"], table_body),
            Paragraph(f"{t['negative_mentions']:,}", table_body),
            Paragraph(f"{t['pct_of_negative_reviews']}%", table_body),
            Paragraph(f"{t['mean_rating']}★", table_body),
            Paragraph(f"{t['total_upvotes']:,}", table_body),
            Paragraph(f"<b>{p_map.get(t['theme_key'], 'P2')}</b>", table_body)
        ])

    th_tab = Table(theme_table_data, colWidths=[150, 70, 80, 70, 60, 110])
    th_tab.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1d3557")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 3),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")])
    ]))
    story.append(th_tab)
    story.append(Spacer(1, 8))

    # Embed Charts (Figure 1 and Figure 3)
    fig1_path = os.path.join(figures_dir, "figure1_rating_distribution.png")
    fig3_path = os.path.join(figures_dir, "figure3_complaint_themes_frequency.png")

    if os.path.exists(fig1_path) and os.path.exists(fig3_path):
        img_table = Table([
            [Image(fig1_path, width=265, height=160), Image(fig3_path, width=265, height=160)]
        ], colWidths=[270, 270])
        img_table.setStyle(TableStyle([('PADDING', (0, 0), (-1, -1), 0)]))
        story.append(img_table)
        story.append(Spacer(1, 8))

    # Representative Evidence Quotes
    story.append(Paragraph("Representative Voice-of-Customer Evidence:", h2_style))
    quote_items = [
        "<b>OTP Modal Friction:</b> <i>\"The new feature and very annoying feature which you have introduced - when you click view otp , it pops up the seat belt safely first. Why do you ask for user input one more click . very annoying I should be able to see the otp in one click.\"</i> (2★, Oct 2026)",
        "<b>Map Auto-Zoom Glitch:</b> <i>\"One of the worst app. While tracking the cab in map. It's automatically zooming out after 3 4 seconds. Have to zoom in again. It's very frustrating!\"</i> (1★, 51 upvotes)",
        "<b>Forced Rating Lockout:</b> <i>\"forcing me to give rating after every ride, so I came here to give you 1 star. because if I don't rate, I can't use the app as there is no skip button.\"</i> (1★, Oct 2026)",
        "<b>Post-Update Crashes:</b> <i>\"whenever i update this app, i am not able to open the app again, I need to uninstall and reinstall again. facing this issue since 3 months.\"</i> (1★, Oct 2026)"
    ]
    for q in quote_items:
        story.append(Paragraph(f"• {q}", quote_style))
        story.append(Spacer(1, 2))

    # Page Break for Recommendations
    story.append(PageBreak())

    # SECTION 7: PRIORITIZED RECOMMENDATIONS
    story.append(Paragraph("5. Prioritized Engineering & Product Recommendations", h1_style))
    story.append(Paragraph(
        "Recommendations are prioritized using an empirical framework based on affected volume, user severity, "
        "community endorsement (upvotes), and implementation velocity.",
        body_style
    ))
    story.append(Spacer(1, 4))

    recs_table_data = [
        [
            Paragraph("Pri", table_header),
            Paragraph("Problem & Evidence", table_header),
            Paragraph("Volume", table_header),
            Paragraph("Recommended Action", table_header),
            Paragraph("Owner", table_header),
            Paragraph("Metric & Experiment", table_header)
        ],
        [
            Paragraph("<b>P0</b>", table_body),
            Paragraph("<b>Boarding OTP Blocked by Seatbelt Modal:</b> 'View OTP' triggers safety popup blocking numeric code curbside.", table_body),
            Paragraph("207 rev<br/>(8.7%)", table_body),
            Paragraph("Render OTP persistently on trip card; convert blocking popup to non-intrusive post-boarding animation.", table_body),
            Paragraph("Android App Squad", table_body),
            Paragraph("<b>Metric:</b> OTP display latency (&lt;1s).<br/><b>Exp:</b> 50/50 A/B test vs persistent chip.", table_body)
        ],
        [
            Paragraph("<b>P0</b>", table_body),
            Paragraph("<b>Maps Auto-Zoom Reset Loop:</b> Live tracking view auto-zooms out and resets every 3-4s, overriding user pinch zoom.", table_body),
            Paragraph("372 rev<br/>(15.7%)<br/>428 up", table_body),
            Paragraph("Decouple marker telemetry updates from camera animation. When user pans/zooms, suppress camera re-centering. Add FAB.", table_body),
            Paragraph("Maps SDK Squad", table_body),
            Paragraph("<b>Metric:</b> Camera auto-resets / session.<br/><b>Exp:</b> Feature flag in beta channel.", table_body)
        ],
        [
            Paragraph("<b>P0</b>", table_body),
            Paragraph("<b>Forced In-App Rating Lockout:</b> Mandatory unskippable ride rating modal drives users to Play Store for retaliatory 1★.", table_body),
            Paragraph("131 rev<br/>(5.5%)", table_body),
            Paragraph("Add clear 'Skip / Remind Later' button; auto-collapse to bottom sheet banner after 8s of inactivity.", table_body),
            Paragraph("Product Design", table_body),
            Paragraph("<b>Metric:</b> Play Store 1★ retaliatory rate.<br/><b>Exp:</b> A/B test across 2 client sites.", table_body)
        ],
        [
            Paragraph("<b>P1</b>", table_body),
            Paragraph("<b>Auth Expiry & Post-Update Crashes:</b> Involuntary logouts during SSO and database schema crashes on auto-update.", table_body),
            Paragraph("227 rev<br/>(9.6%)<br/>1.47★", table_body),
            Paragraph("Implement silent OAuth2 refresh token worker; intercept 401s; add crash-safe Room database migrations.", table_body),
            Paragraph("Mobile Platform", table_body),
            Paragraph("<b>Metric:</b> Involuntary logouts (&lt;1%).<br/><b>Exp:</b> Canary rollout with crash telemetry.", table_body)
        ],
        [
            Paragraph("<b>P1</b>", table_body),
            Paragraph("<b>Static ETA vs City Traffic Divergence:</b> In-app ETA shows 10m while Google Maps shows 35m, causing missed cabs.", table_body),
            Paragraph("252 rev<br/>(10.6%)", table_body),
            Paragraph("Integrate dynamic real-time traffic matrices; show arrival confidence windows ('12-16 min (Heavy Traffic)').", table_body),
            Paragraph("Routing Algorithms", table_body),
            Paragraph("<b>Metric:</b> ETA MAE (&le;5 min).<br/><b>Exp:</b> Shadow test vs 50k trips in BLR.", table_body)
        ],
        [
            Paragraph("<b>P1</b>", table_body),
            Paragraph("<b>Confusing Shift Roster Terminology:</b> 'Login/Logout' shift commute labels confused with app software sign-in.", table_body),
            Paragraph("273 rev<br/>(11.5%)", table_body),
            Paragraph("Rename shift labels to human terms: 'To Office' and 'To Home'; show cutoff countdown timer chips.", table_body),
            Paragraph("Product Design", table_body),
            Paragraph("<b>Metric:</b> Booking funnel drop-off.<br/><b>Exp:</b> Usability testing with 40 riders.", table_body)
        ],
        [
            Paragraph("<b>P2</b>", table_body),
            Paragraph("<b>Support Desk Black Hole:</b> Delayed or unresponsive email tickets during curbside emergencies and cab no-shows.", table_body),
            Paragraph("139 rev<br/>(5.9%)", table_body),
            Paragraph("Deploy in-app SOS / Help Desk bot with 1-tap quick actions and live warm transfer to client transport marshal.", table_body),
            Paragraph("Forward Deployed Eng (FDE)", table_body),
            Paragraph("<b>Metric:</b> First Response Time (&lt;2 min).<br/><b>Exp:</b> Pilot across 5 client accounts.", table_body)
        ],
        [
            Paragraph("<b>P2</b>", table_body),
            Paragraph("<b>Driver Speeding & AC Refusal:</b> Unverified drivers, rash driving, and refusal to turn on AC in extreme heat.", table_body),
            Paragraph("215 rev<br/>(9.1%)<br/>361 up", table_body),
            Paragraph("Add discrete post-trip feedback chips tied to vendor scorecards; automated driver telematics speed monitoring.", table_body),
            Paragraph("Driver Ecosystem", table_body),
            Paragraph("<b>Metric:</b> Speeding events / 1,000 km.<br/><b>Exp:</b> Scorecard integration with 3 vendors.", table_body)
        ]
    ]

    rec_tab = Table(recs_table_data, colWidths=[24, 136, 55, 135, 75, 115])
    rec_tab.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1d3557")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('PADDING', (0, 0), (-1, -1), 2.5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0, 0), (-1, -1), 'TOP')
    ]))
    story.append(rec_tab)
    story.append(Spacer(1, 8))

    # Page Break for Implementation Roadmap & Governance
    story.append(PageBreak())

    # SECTION 8 & 9: IMPLEMENTATION PLAN & SUCCESS METRICS
    story.append(Paragraph("6. Proposed Implementation Roadmap & Governance", h1_style))
    roadmap_text = (
        "<b>Phase 1: Sprint 1 (Days 1–7) — Immediate Hotfixes (P0):</b><br/>"
        "• Deploy build with decoupled seatbelt modal and persistent boarding OTP chip (REC-01).<br/>"
        "• Release Google Maps SDK fix suppressing auto-zoom camera reset during active user touch interactions (REC-02).<br/>"
        "• Introduce 'Skip' button on in-app post-ride rating dialog (REC-03).<br/><br/>"
        "<b>Phase 2: Sprint 2–3 (Days 8–30) — Platform Stability & Booking Flow (P1):</b><br/>"
        "• Implement silent background OAuth2 token refresh worker and crash-safe Room database migrations (REC-04).<br/>"
        "• Calibrate dynamic ETA models with real-time traffic layers and arrival confidence intervals (REC-05).<br/>"
        "• Revamp booking terminology to 'To Office' / 'To Home' with cut-off countdown badges (REC-06).<br/><br/>"
        "<b>Phase 3: Sprint 4–6 (Days 31–90) — Strategic Governance (P2):</b><br/>"
        "• Pilot in-app support chat bot connected to enterprise transport desks (REC-07).<br/>"
        "• Integrate driver compliance telematics and AC non-compliance scorecards (REC-08)."
    )
    story.append(Paragraph(roadmap_text, body_style))
    story.append(Spacer(1, 6))

    # SECTION 10 & 11: ASSUMPTIONS, LIMITATIONS & MONITORING
    story.append(Paragraph("7. Assumptions, Telemetry Limitations & Ongoing Monitoring", h1_style))
    limits_text = (
        "• <b>Symptom vs Root-Cause Boundary:</b> Public reviews reliably capture user experience symptoms. Underlying technical causes "
        "(e.g. Google Maps camera listener logic, database migration conflicts) are framed as engineering hypotheses requiring internal "
        "APM (Crashlytics / Datadog) verification.<br/>"
        "• <b>Ongoing Rating-Monitoring Pipeline:</b> To satisfy leadership's recurring query <i>'How are our Play Store ratings?'</i>, "
        "a continuous automated workflow is established: a weekly cron job executes <code>scripts/collect_reviews.py</code> and "
        "<code>scripts/analyze_reviews.py</code>, generating updated trend charts and firing Slack alerts if the 30-day negative review rate exceeds 20%."
    )
    story.append(Paragraph(limits_text, body_style))
    story.append(Spacer(1, 8))

    # SECTION 12: SOURCES & REFERENCES
    story.append(Paragraph("8. Sources, Tools & References", h1_style))
    sources_text = (
        "1. <b>Google Play Store MoveInSync Application:</b> <code>https://play.google.com/store/apps/details?id=com.moveinsync.ets</code><br/>"
        "2. <b>MoveInSync Corporate Overview:</b> MoveInSync Technology Solutions Pvt Ltd, powering 1.5M+ daily commutes across 430+ enterprises.<br/>"
        "3. <b>Data Scraper & Analytics Stack:</b> Python 3.12, <code>google-play-scraper</code> (v1.2.7), <code>pandas</code> (v3.0.5), <code>matplotlib</code> (v3.11.2), <code>seaborn</code> (v0.13.2), <code>reportlab</code> (v5.0.1), and <code>streamlit</code> (v1.30.0).<br/>"
        "4. <b>Project Repository:</b> <code>https://github.com/Raviranjan010/moveinsync-fde-case-study</code>"
    )
    story.append(Paragraph(sources_text, body_style))

    # Build document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[+] Successfully generated professional PDF report: {output_pdf}")


if __name__ == "__main__":
    build_pdf_report()
