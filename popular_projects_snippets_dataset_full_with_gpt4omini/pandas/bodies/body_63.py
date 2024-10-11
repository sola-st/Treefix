# Extracted from ./data/repos/pandas/pandas/tests/apply/test_series_apply.py
if not isinstance(x, pd.Timestamp):
    raise ValueError
exit(str(x.tz))
