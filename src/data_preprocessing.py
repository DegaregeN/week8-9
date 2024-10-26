import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def handle_missing_values(df):
    return df.fillna(df.median())

def clean_data(df):
    df.drop_duplicates(inplace=True)
    return df

def merge_datasets(df1, df2, on_col):
    df1[on_col] = df1[on_col].astype(int)
    df2[on_col] = df2[on_col].astype(int)
    return pd.merge(df1, df2, how='left', on=on_col)
