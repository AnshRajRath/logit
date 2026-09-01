# Logit

A lightweight Python log-analysis project for exploring user activity data and extracting event-specific records such as logins, logouts, and downloads.

## Overview

Logit is a small cybersecurity/data-analysis exercise built around structured event logs. It reads CSV-based user activity, filters important actions, exports subsets, and summarizes event frequency.

## Current functionality

- Read user activity logs with pandas
- Inspect dataset structure
- Extract login events
- Extract logout events
- Extract download events
- Export filtered records to CSV
- Count activity types

## Repository structure

```text
logit/
├── data/              # Input and generated CSV data
├── src/
│   ├── readlogs.py    # Main log filtering script
│   └── test.py
├── learning.md
├── requirements.txt
└── readme.md
```

## Getting started

```bash
git clone https://github.com/AnshRajRath/logit.git
cd logit
python -m venv .venv
pip install -r requirements.txt
python src/readlogs.py
```

The current script expects `data/users.csv` to contain an `action` column with values such as `login`, `logout`, and `download`.

## Possible next steps

- Add anomaly detection for unusual activity patterns
- Parse timestamps and build session-level features
- Detect repeated failed authentication attempts
- Add visualizations and summary reports
- Extend the project into a small SOC-style log analytics pipeline

## Author

**Ansh Raj Rath**  
GitHub: [@AnshRajRath](https://github.com/AnshRajRath)
