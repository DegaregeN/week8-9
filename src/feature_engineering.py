
import pandas as pd

def add_transaction_frequency(df):
    df['transaction_frequency'] = df.groupby('user_id')['transaction_time'].transform('count')
    return df

def add_time_based_features(df):
    df['hour_of_day'] = pd.to_datetime(df['transaction_time']).dt.hour
    df['day_of_week'] = pd.to_datetime(df['transaction_time']).dt.weekday
    return df
