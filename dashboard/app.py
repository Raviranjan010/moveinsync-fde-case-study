"""Streamlit dashboard: "How are our Play Store ratings?"

Run:  streamlit run dashboard/app.py
Reads data/processed/ (refresh it with: python scripts/refresh_monitoring.py)
"""
from pathlib import Path

import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
st.set_page_config(page_title="MoveInSync Play Store ratings", layout="wide")


@st.cache_data
def load() -> tuple[pd.DataFrame, pd.DataFrame]:
    reviews = pd.read_csv(ROOT / "data/processed/reviews_cleaned.csv", parse_dates=["review_date"])
    issues = pd.read_csv(ROOT / "data/processed/issue_evidence.csv")
    return reviews, issues


df, issues = load()
end = df["review_date"].max()
last90 = df[df["review_date"] > end - pd.Timedelta(days=90)]
prev90 = df[(df["review_date"] <= end - pd.Timedelta(days=90)) & (df["review_date"] > end - pd.Timedelta(days=180))]
last365 = df[df["review_date"] > end - pd.Timedelta(days=365)]


def neg_share(d: pd.DataFrame) -> float:
    return 100 * (d["rating"] <= 2).mean()


st.title("MoveInSync (com.moveinsync.ets): how are the Play Store ratings?")
st.caption(f"Based on {len(df):,} public written reviews, {df['review_date'].min():%b %Y} to {end:%d %b %Y}. "
           "Written reviews skew negative; the store's overall star score is higher (see README).")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Written-review mean (all 8,000)", f"{df['rating'].mean():.2f}")
c2.metric("Last 12 months", f"{last365['rating'].mean():.2f}", f"{neg_share(last365):.1f}% are 1-2 stars", delta_color="off")
c3.metric("Last 90 days", f"{last90['rating'].mean():.2f}",
          f"{last90['rating'].mean() - prev90['rating'].mean():+.2f} vs prior 90 days")
c4.metric("Reply rate on 1-2 star (last 12 months)",
          f"{100 * last365[last365['rating'] <= 2]['developer_reply'].notna().mean():.1f}%")

tab1, tab2, tab3 = st.tabs(["Trend and versions", "What negative reviews say", "Read the reviews"])

with tab1:
    monthly = df.set_index("review_date").resample("MS")["rating"].agg(["mean", "count"])
    monthly = monthly[monthly["count"] >= 30]
    st.subheader("Mean rating of written reviews, by month")
    st.line_chart(monthly["mean"])
    v = df.assign(major=df["app_version"].str.extract(r"^(\d+\.\d+)")[0]).dropna(subset=["major"])
    by_ver = v.groupby("major").agg(reviews=("rating", "size"), mean_rating=("rating", "mean"),
                                    pct_1_2_star=("rating", lambda x: 100 * (x <= 2).mean()))
    by_ver = by_ver[by_ver["reviews"] >= 100].round(2).sort_values("reviews", ascending=False)
    st.subheader("By app version (versions with 100+ reviews)")
    st.dataframe(by_ver)

with tab2:
    st.subheader("Issues named in 1-2 star reviews (keyword rules, multi-label)")
    st.dataframe(issues, hide_index=True)
    st.caption("Counts come from keyword rules in scripts/issue_evidence.py and are not human-labelled. "
               "A review can match several issues. About two thirds of negative reviews name no specific issue.")

with tab3:
    col_a, col_b, col_c = st.columns(3)
    stars = col_a.multiselect("Stars", [1, 2, 3, 4, 5], default=[1, 2])
    since = col_b.date_input("From", value=(end - pd.Timedelta(days=365)).date())
    query = col_c.text_input("Contains word(s)", placeholder="otp, crash, login ...")
    view = df[df["rating"].isin(stars) & (df["review_date"].dt.date >= since)]
    if query:
        view = view[view["review_text"].fillna("").str.contains(query, case=False, regex=False)]
    st.write(f"{len(view):,} reviews")
    st.dataframe(view.sort_values("review_date", ascending=False)[
        ["review_date", "rating", "app_version", "thumbs_up_count", "review_text"]],
        hide_index=True)
