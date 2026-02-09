import pandas as pd

def is_datetime_column(series: pd.Series) -> bool:
    try:
        pd.to_datetime(series.dropna(), errors=="raise")
        return True
    except Exception as e:
        print(e)
        return False