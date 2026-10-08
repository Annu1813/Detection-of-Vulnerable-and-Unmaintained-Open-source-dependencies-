import os
import subprocess
import json

requirements_dir = "requirements_files"
output_dir = "vulnerability_reports"
os.makedirs(output_dir, exist_ok=True)

for file_name in os.listdir(requirements_dir):
    if file_name.endswith(".txt"):
        input_file = os.path.join(requirements_dir, file_name)
        project_name = file_name.replace(".txt", "")  # e.g., proj1
        output_file = os.path.join(output_dir, f"{project_name}_report.json")

        print(f" Auditing {file_name}...")
        
        result = subprocess.run(
            ["pip-audit", "-r", input_file, "-f", "json"],
            capture_output=True,
            text=True
        )
        
        if result.stdout:
            with open(output_file, "w") as f:
                f.write(result.stdout)
            print(f" Report saved: {output_file}")
        else:
            print(f" No output for {file_name} or audit failed.")
