# 🧹 Sales Data Cleaning with Python

This project demonstrates a Python-based approach to cleaning messy sales data using custom functions for field normalization and validation. It prepares raw CSV data for accurate analysis and dashboarding.

## 🗂 Project Structure

```

.
├── data/
│   ├── raw_sales_data_sample.csv       # Sample raw input (anonymized)
│   └── raw_sales_data_sample_cleaned.csv   # Output after cleaning
├── Data_Cleaner.py                     # Main Python script
├── README.md                           # This file
├── .gitignore                          # Git ignored files
├── requirements.txt                    # Python dependencies

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
# 🧹 Sales Data Cleaning with Python

This project demonstrates a Python-based approach to cleaning messy sales data using custom functions for field normalization and validation. It prepares raw CSV data for accurate analysis and dashboarding.

---

## 🧼 Data Cleaning Summary

**Dataset**: `raw_sales_data_sample.csv`  
**Objective**: Clean key fields required for reliable customer and sales analysis. Non-relevant or already-clean columns were excluded from transformation.

---

## 🧾 Overview of Cleaned Columns

| Original Column       | Issues Identified                                                | Cleaning Action                                                         | Cleaned Column            |
|-----------------------|------------------------------------------------------------------|--------------------------------------------------------------------------|---------------------------|
| `Gender`              | Mixed casing, spelling errors, inconsistent labels (e.g., "femail", "M ") | Regex-based normalization to `M`, `F`; unknowns left blank            | `Gender_cleaned`          |
| `Age`                 | Leading zeroes, text-based numbers, out-of-range or missing values | Converted to numeric, kept values between 0–100, others set as `'n/a'` | `Age_cleaned`             |
| `DOB`, `Order Date`, `Delivery Date`, `Signup Date` | Multiple formats (MM/DD/YYYY, DD-MM-YYYY), invalid values                 | Parsed with format detection; invalid entries marked as `'n/a'`         | `[column]_cleaned`        |
| `Quantity Ordered`    | Numeric values embedded in text (e.g., "3 units", "004")          | Extracted digits and converted to integer; invalids replaced with `'n/a'` | `Quantity_Ordered_cleaned` |

---

## 🛠️ Cleaning Techniques Used

- **String normalization**: Lowercasing, trimming whitespace  
- **Regex pattern matching**: To catch misspellings of gender labels  
- **Date parsing logic**: Inferred date formats and validated ranges  
- **Numeric coercion**: Force-converted text numbers, filtered invalids  
- **Invalid/missing handling**: Marked as `'n/a'` or left blank as appropriate  

---

## 📤 Output

Cleaned dataset saved as:  
📁 `raw_sales_data_sample_cleaned.csv`  
- Original columns retained  
- Cleaned versions appended for analysis  
- Ready for aggregation, filtering, and visual reporting  

---

## 🗂 Project Structure


---
