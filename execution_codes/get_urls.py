import pandas as pd
import requests
import time

vuln_df = pd.read_csv("vulnerability_summary.csv")
unique_deps = vuln_df["Dependency"].dropna().unique()

results = []
for dep in unique_deps:
    url = f"https://pypi.org/pypi/{dep}/json"
    try:
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            data = res.json()
            info = data.get("info", {})
            homepage = info.get("home_page", "")
            project_urls = info.get("project_urls", {})
            source_url = project_urls.get("Source", "") or homepage
            results.append({"Dependency": dep, "GitHub_URL": source_url})
        else:
            results.append({"Dependency": dep, "GitHub_URL": "N/A"})
    except Exception as e:
        results.append({"Dependency": dep, "GitHub_URL": "N/A"})
    time.sleep(0.5) 

df = pd.DataFrame(results)
df.to_csv("dependency_github_map.csv", index=False)
print("Saved GitHub links to dependency_github_map.csv")
