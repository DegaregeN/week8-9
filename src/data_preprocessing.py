import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(fraud_data, ip_data, creditcard_data):
    # 1. Handle Missing Values
    def handle_missing(df):
        return df.dropna() if df.isnull().sum().sum() > 0 else df

    # 2. Data Cleaning
    def clean_data(df):
        df = df.drop_duplicates()
        df = df.apply(lambda col: pd.to_datetime(col, errors='ignore') if col.dtypes == 'object' else col)
        return df

    # 3. Exploratory Data Analysis (Simple Summary)
    def perform_eda(df):
        print("\nSummary Statistics:")
        print(df.describe(include='all'))

    # 4. Merge Datasets for Geolocation Analysis
    def merge_ip_country(fraud_df, ip_df):
        ip_df['lower_bound_ip_address'] = ip_df['lower_bound_ip_address'].astype(int)
        ip_df['upper_bound_ip_address'] = ip_df['upper_bound_ip_address'].astype(int)
        fraud_df['ip_address'] = fraud_df['ip_address'].astype(int)
        merged = pd.merge(fraud_df, ip_df, how='left', 
                          left_on='ip_address', 
                          right_on='lower_bound_ip_address')
        return merged

    # 5. Feature Engineering
    def feature_engineering(df):
        df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')
        df['hour_of_day'] = df['transaction_date'].dt.hour
        df['day_of_week'] = df['transaction_date'].dt.dayofweek
        df['transaction_count'] = df.groupby('user_id')['transaction_date'].transform('count')
        return df

    # 6. Normalization and Scaling
    def normalize_data(df):
        scaler = StandardScaler()
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
        return df

    # 7. Encode Categorical Features
    def encode_features(df):
        encoder = LabelEncoder()
        cat_cols = df.select_dtypes(include=['object']).columns
        for col in cat_cols:
            df[col] = encoder.fit_transform(df[col].astype(str))
        return df

    # Apply each preprocessing step
    fraud_data = handle_missing(fraud_data)
    creditcard_data = handle_missing(creditcard_data)
    
    fraud_data = clean_data(fraud_data)
    creditcard_data = clean_data(creditcard_data)
    
    perform_eda(fraud_data)
    
    fraud_data = merge_ip_country(fraud_data, ip_data)
    fraud_data = feature_engineering(fraud_data)
    fraud_data = normalize_data(fraud_data)
    fraud_data = encode_features(fraud_data)

    return fraud_data, creditcard_data

# Ensure the datasets are correctly loaded
try:
    fraud_data = pd.read_csv('Fraud_Data.csv', parse_dates=['transaction_date'])
    ip_data = pd.read_csv('IpAddress_to_Country.csv')
    creditcard_data = pd.read_csv('creditcard.csv')
except FileNotFoundError as e:
    print(f"Error loading datasets: {e}")

# Call the preprocessing function
processed_fraud_data, processed_creditcard_data = preprocess_data(fraud_data, ip_data, creditcard_data)

# Save the processed data for further analysis or model training
processed_fraud_data.to_csv('cleaned_fraud_data.csv', index=False)
processed_creditcard_data.to_csv('creditcard_data.csv', index=False)

