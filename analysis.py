"""
Taobao Shopper Behavior Analysis
Question: Where do Taobao shoppers drop off between viewing a product and
buying it, and what do buyers do differently?

Run from the folder that contains UserBehavior.csv:
    python analysis.py
"""

import os

import matplotlib.pyplot as plt
import pandas as pd

RAW_FILE = "UserBehavior.csv"
SAMPLE_FILE = "sample.csv"
N_ROWS = 2_000_000
COLUMNS = ["user_id", "item_id", "category_id", "behavior", "timestamp"]


def load_sample():
    """Load the first N_ROWS rows of the raw file (or reuse the saved sample)."""
    if os.path.exists(SAMPLE_FILE):
        return pd.read_csv(SAMPLE_FILE)
    df = pd.read_csv(RAW_FILE, nrows=N_ROWS, header=None, names=COLUMNS)
    df.to_csv(SAMPLE_FILE, index=False)
    return df


def action_funnel(df):
    """Count actions (views, cart adds, purchases) and plot the funnel."""
    counts = df["behavior"].value_counts()
    print("Action counts:")
    print(counts)
    print(f"Cart adds / views: {counts['cart'] / counts['pv']:.1%}")
    print(f"Purchases / cart adds: {counts['buy'] / counts['cart']:.1%}")
    print(f"Purchases per 100 views: {counts['buy'] / counts['pv'] * 100:.1f}")

    counts[["pv", "cart", "buy"]].plot(kind="bar", title="Shopper funnel (sample)")
    plt.tight_layout()
    plt.savefig("funnel.png")
    plt.close()


def purchases_by_hour(df):
    """Plot purchases by hour of day, converted to China time (UTC+8)."""
    buys = df[df["behavior"] == "buy"].copy()
    buys["hour"] = (
        pd.to_datetime(buys["timestamp"], unit="s") + pd.Timedelta(hours=8)
    ).dt.hour
    buys["hour"].value_counts().sort_index().plot(
        kind="bar", title="Purchases by hour of day (China time)"
    )
    plt.tight_layout()
    plt.savefig("hours.png")
    plt.close()


def user_funnel(df):
    """Count unique users at each step instead of actions."""
    users = df.groupby("behavior")["user_id"].nunique()
    print("\nUnique users per behavior:")
    print(users)
    print(f"Users who bought: {users['buy'] / users['pv']:.1%} of users who viewed")


if __name__ == "__main__":
    data = load_sample()
    action_funnel(data)
    purchases_by_hour(data)
    user_funnel(data)
    print("\nSaved funnel.png and hours.png")
