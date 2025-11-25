import pandas as pd
import numpy as np

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully. Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def handle_missing_values(df):
    print("\n--- Handling Missing Values ---")
    print("Missing values before cleaning:")
    print(df.isnull().sum())
    
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())
    
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else 'Unknown')
    
    print("Missing values after cleaning:")
    print(df.isnull().sum())
    return df

def standardize_columns(df):
    print("\n--- Standardizing Columns ---")
    
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('[^a-z0-9_]', '', regex=True)
    print(f"Cleaned column names: {list(df.columns)}")
    
    text_cols = df.select_dtypes(include=['object']).columns
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip().str.title()
    
    return df

def fix_data_types(df):
    print("\n--- Fixing Data Types ---")
    print("Data types before fixing:")
    print(df.dtypes)
    
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='ignore')
    
    date_columns = [col for col in df.columns if 'date' in col.lower()]
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    
    print("Data types after fixing:")
    print(df.dtypes)
    return df

def save_cleaned_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"\nCleaned data saved to: {output_path}")

def main():
    input_file = "assest/amazon.csv"
    output_file = "cleaned_data.csv"
    
    df = load_data(input_file)
    if df is None:
        return
    
    print("Initial data info:")
    print(df.info())
    print("\nFirst 5 rows:")
    print(df.head())
    
    df = handle_missing_values(df)
    df = standardize_columns(df)
    df = fix_data_types(df)
    
    print("\n--- Final Data Summary ---")
    print(f"Final shape: {df.shape}")
    print("\nData types:")
    print(df.dtypes)
    print("\nFirst 5 rows of cleaned data:")
    print(df.head())
    
    save_cleaned_data(df, output_file)

if __name__ == "__main__":
    main()