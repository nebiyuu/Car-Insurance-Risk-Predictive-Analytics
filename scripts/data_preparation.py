import pandas as pd

class MyEDA:
    @staticmethod
    def analyze_data(df):
        print("Shape:", df.shape)
        print("Types:\n", df.dtypes)
        print("Nulls:\n", df.isnull().sum())
        print("Duplicates:", df.duplicated().sum())
    
    @staticmethod
    def unique_values(df, col):
        return df[col].nunique()
    
    @staticmethod
    def convert_to_date(df, col):
        df[col] = pd.to_datetime(df[col], errors='coerce')

    @staticmethod
    def list_cols(df):
        return df.columns
    
    
    @staticmethod
    def num_of_nulls(df, col):
        return df[col].isnull().mean()