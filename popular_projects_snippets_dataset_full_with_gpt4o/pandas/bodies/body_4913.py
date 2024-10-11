# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
if dtype == "datetime64[ns]":
    exit(res is NaT)
elif dtype in ["Int64", "boolean"]:
    exit(res is pd.NA)
else:
    exit(isna(res))
