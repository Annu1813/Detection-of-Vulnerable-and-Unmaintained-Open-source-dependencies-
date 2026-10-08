import pandas as pd
from datetime import datetime

df = pd.read_csv("github_activity_metrics.csv")

today = pd.to_datetime(datetime.utcnow())

df['last_commit_date'] = pd.to_datetime(df['last_commit_date'], utc=True)
df['days_since_commit'] = (today - df['last_commit_date'].dt.tz_convert(None)).dt.days

def score_commit_gap(days):
    if days <= 30:
        return 0
    elif days <= 90:
        return 3
    elif days <= 180:
        return 5
    elif days <= 365:
        return 7
    else:
        return 10

def score_commit_freq(commits):
    if commits > 30:
        return 0
    elif commits > 10:
        return 3
    elif commits > 5:
        return 5
    elif commits > 0:
        return 7
    else:
        return 10

def score_contributors(contribs):
    if contribs > 10:
        return 0
    elif contribs > 5:
        return 3
    elif contribs > 2:
        return 5
    elif contribs > 0:
        return 7
    else:
        return 10

def score_releases(releases):
    if releases > 20:
        return 0
    elif releases > 10:
        return 3
    elif releases > 5:
        return 5
    elif releases > 0:
        return 7
    else:
        return 10

df["risk_commit_gap"] = df["days_since_commit"].apply(score_commit_gap)
df["risk_commit_freq"] = df["Recent Commits (6mo)"].apply(score_commit_freq)
df["risk_contributors"] = df["Contributors (6mo)"].apply(score_contributors)
df["risk_releases"] = df["Total Releases"].apply(score_releases)

df["ARS"] = df[["risk_commit_gap", "risk_commit_freq", "risk_contributors", "risk_releases"]].mean(axis=1)
df["ARS"] = df["ARS"].round(2)

df[["Dependency", "ARS"]].to_csv("ars_scores.csv", index=False)
print(" ARS scores saved to ars_scores.csv")