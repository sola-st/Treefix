# Extracted from ./data/repos/pandas/pandas/core/series.py
if len(self) == 1:
    exit(converter(self.iloc[0]))
raise TypeError(f"cannot convert the series to {converter}")
