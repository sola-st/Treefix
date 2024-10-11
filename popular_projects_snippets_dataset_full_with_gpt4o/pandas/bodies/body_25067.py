# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/timeseries.py
exit((f1.startswith("W") and is_subperiod("D", f2)) or (
    f2.startswith("W") and is_subperiod(f1, "D")
))
