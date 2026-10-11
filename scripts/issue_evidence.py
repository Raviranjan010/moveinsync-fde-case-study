"""Issue-level evidence for the recommendation memo.

Counts how many 1-2 star reviews mention each specific, fixable issue
(keyword rules, multi-label). Counts are NOT human-validated; use
--samples N to print random matches per issue and check them by eye.

Usage:
    python scripts/issue_evidence.py            # writes data/processed/issue_evidence.csv
    python scripts/issue_evidence.py --samples 5
"""
import argparse
import warnings

import re
from pathlib import Path

import pandas as pd

warnings.filterwarnings("ignore", message="This pattern is interpreted")
ROOT = Path(__file__).resolve().parents[1]
CLEAN = ROOT / "data" / "processed" / "reviews_cleaned.csv"
OUT = ROOT / "data" / "processed" / "issue_evidence.csv"
FIG = ROOT / "reports" / "figures" / "issues_last_12_months.png"

ISSUES = {
    "App crashes / won't open / stuck on error":
        r"crash|not opening|won'?t open|doesn'?t open|not able to open|unable to open|force close|keeps closing|app (is )?(closing|closes)|white screen|blank screen|something went wrong|not loading|hang(s|ing)?\b|freez",
    "Login / session problems (repeated login, SSO, locked out)":
        r"log ?in(?! (time|shift|trip|slot))|log ?out(?! (time|shift|trip|slot))|logged out|sign ?in|\bsso\b|session expired|password",
    "OTP not received / OTP issues":
        r"\botp",
    "Live tracking / map (zoom reset, wrong location, not updating)":
        r"zoom|track(ing)? (is |does|not|doesn|isn|fail|issue|problem|work)|not track|live (location|track)|\bgps\b|wrong location|location (is )?(not|wrong|incorrect)|map (is |keeps|auto|not)|not updating|not moving|real ?-?time",
    "ETA / pickup time wrong":
        r"\beta\b|arrival time|pick-?up time",
    "Booking / roster failures (can't book, slot, roster)":
        r"unable to book|not able to book|can'?t book|cannot book|booking (fail|issue|problem|error|not|difficult)|not allowing (me )?to book|roster|\bslot",
    "Cab late / no-show / driver didn't come":
        r"no[- ]?show|did ?n'?t (come|arrive|turn)|never (came|arrived|turned)|not (come|arrive|turn)|(cab|driver|vehicle|bus|shuttle) (is |was )?(late|delayed)|always late|waiting for (the )?(cab|driver|bus|shuttle|vehicle)",
    "Support / complaint not resolved":
        r"customer (care|support|service)|help ?desk|helpline|no (one )?(respon|help|reply)|not respon|no support|raise (a )?(complaint|ticket)|ticket|escalat",
    "Driver conduct / safety / AC":
        r"rude|misbehav|behaviou?r|rash|over ?speed|drunk|alcohol|unsafe|harass|\bac (is )?(not|off)|no ac|air ?condition|refus",
    "Seat-belt prompt before OTP":
        r"seat ?-?belt|buckle",
    "Forced / repeated rating prompt":
        r"(rate|rating|feedback).{0,50}(force|mandatory|compel|every|again|skip|compuls)|(force|mandatory|compel|compuls|every time|skip).{0,50}(rate|rating|feedback)",
    "Ads / new update disliked":
        r"\bads?\b|advert|new update|latest update|after (the )?update|update (is|was)",
}


def load_reviews() -> pd.DataFrame:
    df = pd.read_csv(CLEAN, parse_dates=["review_date"])
    return df


def count_issues(neg: pd.DataFrame):
    text = neg["review_text"].fillna("").str.lower()
    masks = {name: text.str.contains(pat, regex=True) for name, pat in ISSUES.items()}
    anyspecific = pd.concat(masks.values(), axis=1).any(axis=1)
    return masks, anyspecific


def make_chart(out: pd.DataFrame, window_days: int, n_neg: int) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    col = f"recent_{window_days}d_neg"
    d = out[~out["issue"].str.startswith("No specific")].sort_values(col).tail(8)
    fig, ax = plt.subplots(figsize=(8, 3.8))
    ax.barh(d["issue"].str.replace(r" \(.*\)", "", regex=True), d[col], color="#2b6cb0")
    for y, v in enumerate(d[col]):
        ax.text(v + 0.8, y, f"{v} ({100 * v / n_neg:.0f}%)", va="center", fontsize=8)
    ax.set_xlabel(f"1-2 star reviews naming the issue (last {window_days} days, n={n_neg} negative reviews)", fontsize=8)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=8)
    ax.set_xlim(0, d[col].max() * 1.25)
    fig.tight_layout()
    FIG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG, dpi=200)
    plt.close(fig)


def main(samples: int = 0, window_days: int = 365) -> pd.DataFrame:
    df = load_reviews()
    cutoff = df["review_date"].max() - pd.Timedelta(days=window_days)
    neg_all = df[df["rating"] <= 2]
    neg_rec = neg_all[neg_all["review_date"] > cutoff]
    m_all, any_all = count_issues(neg_all)
    m_rec, any_rec = count_issues(neg_rec)
    rows = []
    for name in ISSUES:
        rows.append({
            "issue": name,
            f"recent_{window_days}d_neg": int(m_rec[name].sum()),
            "recent_pct_of_neg": round(100 * m_rec[name].mean(), 1),
            "alltime_neg": int(m_all[name].sum()),
            "alltime_pct_of_neg": round(100 * m_all[name].mean(), 1),
        })
    rows.append({
        "issue": "No specific issue named (rules matched nothing)",
        f"recent_{window_days}d_neg": int((~any_rec).sum()),
        "recent_pct_of_neg": round(100 * (~any_rec).mean(), 1),
        "alltime_neg": int((~any_all).sum()),
        "alltime_pct_of_neg": round(100 * (~any_all).mean(), 1),
    })
    out = pd.DataFrame(rows).sort_values(f"recent_{window_days}d_neg", ascending=False)
    out.to_csv(OUT, index=False)
    make_chart(out, window_days, len(neg_rec))
    print(f"Negative (1-2 star) reviews: all-time {len(neg_all)}, last {window_days} days {len(neg_rec)} "
          f"(since {cutoff.date()})")
    print(out.to_string(index=False))
    if samples:
        for name, m in m_rec.items():
            print(f"\n--- {name} (recent) ---")
            for t in neg_rec.loc[m, "review_text"].sample(min(samples, int(m.sum())), random_state=1):
                print(" *", re.sub(r"\s+", " ", t)[:220])
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--samples", type=int, default=0)
    ap.add_argument("--window-days", type=int, default=365)
    a = ap.parse_args()
    main(a.samples, a.window_days)
