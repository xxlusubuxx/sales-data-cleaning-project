import pandas as pd
from datetime import datetime

df = pd.read_csv("data/raw_sales_data_sample.csv")

# Print unique values for each specified header
print("Unique values per column:")
columns_to_check = [
    "Transaction_ID", "Cust Name", "Email Address", "Phone#", "Gender", "Age", "DOB", "Region",
    "Order Date", "Delivery Date", "Product Category", "Product_ID", "Quantity Ordered",
    "Unit Price", "Total Amount", "Promo Code", "Channel", "Referral Source", "Signup Date",
    "Subscribed To Newsletter", "Feedback", "Satisfaction Score"
]
for col in columns_to_check:
    if col in df.columns:
        print(f"{col}: {df[col].unique()[:10]}{' ...' if len(df[col].unique()) > 10 else ''}")
    else:
        print(f"{col}: Column not found in DataFrame")

def clean_gender(df: any) -> None:
    # Normalize casing and strip leading/trailing whitespace
    df['Gender_cleaned'] = df['Gender'].astype(str).str.strip().str.lower()
    # Final standardization: catch clean entries like "female" and "male" that didn’t match regex
    df['Gender_cleaned'] = df['Gender_cleaned'].replace({
        'female': 'F',
        'male': 'M'
    })

    # Replace "female" and its typos with 'F'
    df['Gender_cleaned'] = df['Gender_cleaned'].str.replace(
        r'\b(f(e|3)?(e|3)?m?[a@]l(e|3)?)\b', 'F', regex=True
    )
    # Replace "male" and its typos with 'M'
    df['Gender_cleaned'] = df['Gender_cleaned'].str.replace(
        r'\b(m[a@]l(e|3)?)\b', 'M', regex=True
    )
    # Final standardization: catch clean entries like "female" and "male" that didn’t match regex
    df['Gender_cleaned'] = df['Gender_cleaned'].replace({
        'female': 'F',
        'male': 'M',
        'f': 'F',
        'm': 'M',
    })

    # If the cleaned value is not one of our expected values, assign ''
    valid_values = ['F', 'M']
    df['Gender_cleaned'] = df['Gender_cleaned'].apply(lambda x: x if x in valid_values else '')

    # Optional: Check your results
    print(df['Gender_cleaned'].value_counts())

def clean_age(df: any) -> None:
    # Example setup: make sure Age is string for safe processing
    df['Age_cleaned'] = df['Age'].astype(str).str.strip()

    # Remove leading zeros (but preserve valid '0')
    df['Age_cleaned'] = df['Age_cleaned'].str.lstrip('0')

    # Replace empty strings (from lstrip) with '0'
    df['Age_cleaned'] = df['Age_cleaned'].replace('', '')

    # Convert to numeric, force errors to NaN
    if len(df['Age_cleaned']) > 1:
        df['Age_cleaned'] = pd.to_numeric(df['Age_cleaned'], errors='coerce')

    # Replace out-of-range or invalid with ''
    df['Age_cleaned'] = df['Age_cleaned'].apply(lambda x: x if pd.notnull(x) and 0 <= x <= 100 else '')

    # Optional: convert to string if needed
    df['Age_cleaned'] = df['Age_cleaned'].astype(str)

    # Check what's in the column now
    print("Unique cleaned ages:")
    print(df['Age_cleaned'].unique())

def clean_birthday(dob_str):
    if not isinstance(dob_str, str):
        return ''
    
    dob_str = dob_str.strip()
    
    # Detect separator
    if '/' in dob_str:
        parts = dob_str.split('/')
    elif '-' in dob_str:
        parts = dob_str.split('-')
    else:
        return ''
    
    if len(parts) != 3:
        return ''
    
    try:
        # Try m/d/yyyy
        month, day, year = map(int, parts)
        
        if month > 12 and day <= 12:
            # Switch day and month, assume it's d/m/yyyy
            day, month = month, day
        
        if not (1 <= month <= 12 and 1 <= day <= 31):
            return ''

        # Validate final date
        datetime(year, month, day)  # will raise ValueError if invalid
        return f"{month:02d}-{day:02d}-{year:04d}"
    
    except Exception:
        return ''
    
def clean_order_date(dob_str):
    if not isinstance(dob_str, str):
        return ''
    
    dob_str = dob_str.strip()
    
    # Detect separator
    if '/' in dob_str:
        parts = dob_str.split('/')
    elif '-' in dob_str:
        parts = dob_str.split('-')
    else:
        return ''
    
    if len(parts) != 3:
        return ''
    
    try:
        # Try m/d/yyyy
        month, day, year = map(int, parts)
        
        if month > 12 and day <= 12:
            # Switch day and month, assume it's d/m/yyyy
            day, month = month, day
        
        if not (1 <= month <= 12 and 1 <= day <= 31):
            return ''
        year = 2025
        # Validate final date
        datetime(year, month, day)  # will raise ValueError if invalid
        return f"{month:02d}-{day:02d}-{year:04d}"
    
    except Exception:
        return ''
    
def clean_quantity_ordered(quantity_str):
    if not isinstance(quantity_str, str):
        return ''
    
    quantity_str = quantity_str.strip().lower()
    
    # Mapping for number words up to 100
    number_words = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
        'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
        'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 'hundred': 100
    }

    # Try to convert text numbers like "twenty one"
    words = quantity_str.replace('-', ' ').split()
    total = 0
    for word in words:
        if word in number_words:
            if word == 'hundred' and total != 0:
                total *= 100
            else:
                total += number_words[word]
    if total > 0:
        quantity = total
    else:
        # Remove non-numeric characters and try to convert
        cleaned_quantity = ''.join(filter(str.isdigit, quantity_str))
        if not cleaned_quantity:
            return ''
        try:
            quantity = int(cleaned_quantity)
        except ValueError:
            return ''

    # Only allow whole numbers up to 100
    if 0 <= quantity <= 100:
        return quantity
    else:
        return ''

# Apply gender cleaner
clean_gender(df)

# Apply age cleaner
clean_age(df)

# Apply birthday cleaner to all relevant date columns
date_columns = ["DOB", "Order Date", "Delivery Date", "Signup Date"]
for col in date_columns:
    if col in df.columns and col != "DOB":
        df[f"{col}_cleaned"] = df[col].apply(clean_order_date)
    else:
        df[f"{col}_cleaned"] = df[col].apply(clean_birthday)

# Apply quantity cleaner
if "Quantity Ordered" in df.columns:
    df["Quantity_Ordered_cleaned"] = df["Quantity Ordered"].apply(clean_quantity_ordered)

# Save to new CSV
df.to_csv("data/raw_sales_data_sample_cleaned.csv", index=False)
print("Cleaned data saved to MOCK_DATA_cleaned.csv")
