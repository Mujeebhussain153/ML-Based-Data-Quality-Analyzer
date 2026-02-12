from column_profiler import profile_column
import pandas as pd

def profile_dataset(df: pd.DataFrame) -> dict:
    try:
        data_set_profile = {}
        for col in df.columns:
            data_set_profile[col] = profile_column(df[col])
        return data_set_profile
    except Exception as e:
        print(f"Error profiling dataset: {e}")
        return None