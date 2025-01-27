# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_datetime.py
assert DatetimeIndex([np.nan])[0] is pd.NaT
