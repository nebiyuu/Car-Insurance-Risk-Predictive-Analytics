import pandas as pd
print("load_data loaded")

def load_data(file_path):
    df = pd.read_csv(file_path, sep='|')
    return df

def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df