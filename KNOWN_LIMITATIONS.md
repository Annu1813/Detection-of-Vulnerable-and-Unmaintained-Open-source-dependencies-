# Known limitations and reproducibility status

This repository preserves the original student project artefacts; **no claim is made that the full pipeline has been successfully rerun in this packaged layout**.

1. `phase1B.py` writes `CVSS = 0` for all vulnerabilities, so the final score does not reflect real CVSS severity.
2. `phase3A_final_score.py` computes `0.6 * CVSS + 0.4 * ARS`, but uses thresholds `0.4` and `0.7` on a scale potentially extending to 10. The risk classes should not be used as calibrated security labels.
3. The original scripts read/write files from the working directory. In this repository, original inputs, scripts and historical outputs have been grouped into subfolders for presentation. Adjust paths before rerunning.
4. `step2A_github_activity.py` writes `Last Commit Date`, while the supplied historical CSV and downstream scripts use `last_commit_date`. The original scripts and supplied dataset therefore do not share a consistent schema.
5. GitHub API results may be limited by pagination, API rate limits, missing data, repository redirects or project URL mapping errors.
6. `eval_ground_truth.py` uses last-commit recency as a proxy for abandonment, not an independently verified ground-truth label.
7. Some requirement lists are intentionally old or malformed; `pip-audit` may fail on them. Audit failure is not evidence of zero vulnerabilities.
8. CSV and notebook findings reflect the original collection period and should not be presented as live results. Notebook execution outputs may be historical.
9. No automated end-to-end tests or repeatable environment lockfile are supplied.

## Responsible interpretation

Use the included files for learning, inspection and demonstrating the workflow. Verify current advisory data, package identity and maintenance status before making security decisions.
