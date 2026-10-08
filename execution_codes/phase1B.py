import os
import json
import csv

INPUT_FOLDER = "vulnerability_reports"
OUTPUT_CSV = "vulnerability_summary.csv"

all_rows = []

for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith("_report.json"):
        filepath = os.path.join(INPUT_FOLDER, filename)
        project_name = filename.split("_report.json")[0]

        with open(filepath, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(f"Skipping {filename} due to JSON error")
                continue

        dependencies = data.get("dependencies", [])
        for dep in dependencies:
            name = dep.get("name", "")
            version = dep.get("version", "")
            vulns = dep.get("vulns", [])

            if not vulns:
                all_rows.append([project_name, name, version, "No CVE", 0, "No known vulnerabilities"])
            else:
                for v in vulns:
                    cve = v.get("id", "Unknown")
                    desc = v.get("description", "")[:150] 
                    all_rows.append([project_name, name, version, cve, 0, desc])

with open(OUTPUT_CSV, "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Project", "Dependency", "Version", "CVE ID", "CVSS", "Description"])
    writer.writerows(all_rows)

print(f"Summary CSV written to: {OUTPUT_CSV}")
