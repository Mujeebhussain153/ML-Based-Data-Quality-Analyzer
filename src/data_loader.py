import pandas as pd
import os

class DataLoader:
    def __init__(self):
        pass

    def load_data(self, file_path):
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File not found: {file_path}")
            df = pd.read_csv(file_path)
            return df
        except Exception as e:
            print(f"Error loading data: {e}")
            return None


if __name__ == "__main__":
    loader = DataLoader()
    df = loader.load_data(r"..\data\WA_Fn-UseC_-Telco-Customer-Churn.csv")
    if df.empty:
        print("DataFrame is empty")
    else:
        print(df.head())