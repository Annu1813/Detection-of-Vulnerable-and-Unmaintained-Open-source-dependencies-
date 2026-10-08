
import csv
import requests
import time

GITHUB_TOKEN = ""  

headers = {
    "Accept": "application/vnd.github+json"
}
if GITHUB_TOKEN:
    headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

def extract_owner_repo(url):
    try:
        parts = url.strip().rstrip("/").split("/")
        owner = parts[-2]
        repo = parts[-1]
        return owner, repo
    except Exception:
        return None, None

def get_last_commit(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url, headers=headers)
    if response.ok and response.json():
        return response.json()[0]["commit"]["committer"]["date"]
    return "N/A"

def get_recent_commit_count(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    since = time.strftime("%Y-%m-%dT00:00:00Z", time.gmtime(time.time() - 180 * 86400))
    response = requests.get(url, headers=headers, params={"since": since})
    if response.ok:
        return len(response.json())
    return 0

def get_contributors(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/contributors"
    response = requests.get(url, headers=headers)
    if response.ok:
        return len(response.json())
    return 0

def get_release_count(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    response = requests.get(url, headers=headers)
    if response.ok:
        return len(response.json())
    return 0

input_file = "dependency_github_map.csv"
output_file = "github_activity_metrics.csv"

with open(input_file, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

metrics = []

for row in rows:
    dep = row["Dependency"]
    url = row["GitHub_URL"]
    owner, repo = extract_owner_repo(url)
    print(f"Processing: {dep} → {owner}/{repo}")
    if not owner or not repo:
        metrics.append([dep, url, "N/A", 0, 0, 0])
        continue

    last_commit = get_last_commit(owner, repo)
    commit_count = get_recent_commit_count(owner, repo)
    contributor_count = get_contributors(owner, repo)
    release_count = get_release_count(owner, repo)
    metrics.append([dep, url, last_commit, commit_count, contributor_count, release_count])
    time.sleep(1)

with open(output_file, "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Dependency", "GitHub_URL", "Last Commit Date", "Recent Commits (6mo)", "Contributors (6mo)", "Total Releases"])
    writer.writerows(metrics)

print(f"Done. Output saved to {output_file}")
