# Dependency Vulnerability & Maintenance Analyzer

A Python-based exploratory cybersecurity project examining **known dependency vulnerabilities** and **open-source maintenance activity**. The workflow combines `pip-audit` findings with repository activity metrics to explore a composite dependency risk score.

## What I built

- Collected Python dependency requirement files for 15 sample projects.
- Ran a `pip-audit`-based vulnerability scanning stage and summarised its findings.
- Mapped packages to project URLs and collected GitHub activity indicators.
- Computed an **Abandonment Risk Score (ARS)** using commit recency, recent commits, contributors and releases.
- Combined vulnerability and maintenance information into a prototype risk score, then explored the resulting data in Jupyter notebooks.

## Repository contents

| Directory | Purpose |
| --- | --- |
| `input_files/` | Fifteen sample dependency lists (`proj*.txt`) |
| `execution_codes/` | Original Python pipeline scripts |
| `csv_files/` | Saved historical output datasets |
| `analysis/` | Original exploratory Jupyter notebooks |

## Original workflow

The original scripts expect to be run from the project working directory with the following file locations:

1. Copy the input `proj*.txt` files into a directory named `requirements_files/`.
2. Run `phase1_security_audit.py` to generate JSON files in `vulnerability_reports/` (requires `pip-audit`).
3. Run `phase1B.py` to produce `vulnerability_summary.csv`.
4. Run `get_urls.py` to produce `dependency_github_map.csv`.
5. Run `step2A_github_activity.py` to produce `github_activity_metrics.csv`.
6. Run `phase2B_compute_ars.py` to produce `ars_scores.csv`.
7. Run `phase3A_final_score.py` to produce `final_dependency_risk_scores.csv`.
8. Run `eval_ground_truth.py` and inspect the notebooks for exploratory analysis.

**Important:** The code is preserved in its original form; paths and some output field names differ from the organised repository layout. This is a research snapshot, **not a verified one-command runnable application**. See [Known limitations](KNOWN_LIMITATIONS.md) before reproducing or relying on any scores.

## Tools and techniques

Python, `pip-audit`, `pandas`, `requests`, GitHub REST API, Jupyter notebooks, CSV-based analysis.

## Security relevance

Known-vulnerability checks help identify packages that may need upgrades. Maintenance activity can provide additional context for dependency review, but low activity **does not by itself prove a package is insecure or abandoned**.

## Results and limitations

The included CSV files are **historical project outputs**, not current vulnerability or repository-status assessments. The prototype's CVSS values and score thresholds need correction before its `Risk Level` column can be treated as meaningful. The supplied labels are heuristic, not independently validated ground truth. This repository demonstrates an investigative workflow and its development stage; it should not be used to make production security decisions.

## Next improvements

- Populate verified severity scores or explicitly treat unavailable CVSS as unknown.
- Calibrate risk thresholds to the actual scoring scale.
- Normalise GitHub URL handling, pagination and API failure cases.
- Make the workflow reproducible with consistent paths, configuration and automated tests.
- Validate against independently labelled maintenance outcomes.
