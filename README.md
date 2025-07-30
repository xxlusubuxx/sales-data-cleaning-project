# 🧹 Sales Data Cleaning with Python

This project demonstrates a Python-based approach to cleaning messy sales data using custom functions for field normalization and validation. It prepares raw CSV data for accurate analysis and dashboarding.

## 🗂 Project Structure

```

.
├── data/
│   ├── raw\_sales\_data\_sample.csv       # Sample raw input (anonymized)
│   └── cleaned\_sales\_data\_sample.csv   # Output after cleaning
├── Data\_Cleaner.py                     # Main Python script
├── README.md                           # This file
├── .gitignore                          # Git ignored files
├── requirements.txt                    # Python dependencies
└── LICENSE                             # (Optional) License

## 🛠 What This Script Does

- Cleans up inconsistent gender, age, and date formats
- Detects and corrects swapped month/day values
- Converts number words like `"twenty one"` into integers
- Validates entries to ensure clean, analysis-ready output

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
````

## ▶️ How to Run

```bash
python Data_Cleaner.py
```

Make sure the input CSV is placed in the correct path (or update the path in the script).

## 📊 Output

The script outputs a cleaned CSV file ready for loading into Power BI or another BI tool for analysis.

---

**Note**: All data used here is mock data, anonymized and for demonstration purposes only.

````

---
