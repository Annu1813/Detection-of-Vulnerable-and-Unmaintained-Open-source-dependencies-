import pandas as pd

vuln_df = pd.read_csv("vulnerability_summary.csv")
ars_df = pd.read_csv("ars_scores.csv")

merged_df = pd.merge(vuln_df, ars_df, on="Dependency", how="inner")

merged_df['CVSS'] = merged_df['CVSS'].fillna(0)
merged_df['ARS'] = merged_df['ARS'].fillna(0)

merged_df["Final Risk Score"] = (0.6 * merged_df["CVSS"]) + (0.4 * merged_df["ARS"])

def classify_risk(score):
    if score >= 0.7:
        return "High"
    elif score >= 0.4:
        return "Medium"
    else:
        return "Low"

merged_df["Risk Level"] = merged_df["Final Risk Score"].apply(classify_risk)

merged_df.to_csv("final_dependency_risk_scores.csv", index=False)

print(" Final risk scores calculated and saved to 'final_dependency_risk_scores.csv'")
