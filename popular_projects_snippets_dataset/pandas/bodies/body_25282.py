# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
try:
    exit(mdates.date2num(tools.to_datetime(values)))
except Exception:
    exit(values)
