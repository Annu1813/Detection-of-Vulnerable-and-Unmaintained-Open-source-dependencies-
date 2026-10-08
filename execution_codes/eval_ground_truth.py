import pandas as pd
from datetime import datetime

risk_df = pd.read_csv("final_dependency_risk_scores.csv")
activity_df = pd.read_csv("github_activity_metrics.csv")

activity_df["last_commit_date"] = pd.to_datetime(activity_df["last_commit_date"], utc=True)
activity_df["last_commit_date"] = activity_df["last_commit_date"].dt.tz_localize(None)

merged_df = pd.merge(
    risk_df,
    activity_df[["Dependency", "last_commit_date"]],
    left_on="Dependency",
    right_on="Dependency",
    how="left"
)

def label_ground_truth(last_commit_date):
    if pd.isnull(last_commit_date):
        return "Unknown"
    days_since_commit = (datetime.utcnow() - last_commit_date).days
    return "Abandoned" if days_since_commit > 365 else "Active"

merged_df["ground_truth"] = merged_df["last_commit_date"].apply(label_ground_truth)

merged_df.to_csv("phase4A_ground_truth_labeled.csv", index=False)
print(" Ground truth labels saved to 'phase4A_ground_truth_labeled.csv'")
