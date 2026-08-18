import pandas as pd


def analyze_data(df: pd.DataFrame) -> dict:
    return {
        "mean": df.mean(numeric_only=True).to_dict(),
        "sum": df.sum(numeric_only=True).to_dict()
    }

