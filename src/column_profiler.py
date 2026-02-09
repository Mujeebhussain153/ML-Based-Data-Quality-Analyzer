from openpyxl.chart.title import title_maker
import numpy as np
import pandas as pd
from utils import is_datetime_column

def profile_column(series: pd.Series) -> dict:
    try:
        profile = {}
        total_count = len(series)
        non_null = series.dropna()
        unique_count = non_null.nunique()
        profile["missing_count"] = total_count - len(non_null)
        profile["missing_pct"] = profile["missing_count"]/total_count
        profile["unique_count"] = unique_count
        profile["unique_pct"] = profile["unique_count"]/ total_count
        profile["d_type"] = str(series.dtype)

        if is_datetime_column(series):
            profile["inferred_type"] = "datetime"
            return profile

        if np.issubdtype(series.dtype, np.number):
            if profile["unique_pct"] > 0.9:
                profile["inferred_type"] = "identifier"
            else:
                profile["inferred_type"] = "numerical"
            return profile

        try:
            pd.to_numeric(non_null)
            profile["inferred_type"] = "numerical_text"
            return profile
        except:
            pass
        
    except Exception as e:
        print(f"Error profiling column: {e}")
        return None
    