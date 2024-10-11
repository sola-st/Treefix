# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimes.py
# make sure we accept datetime64 and datetime in addition to Timestamp
dti = pd.date_range("2000", periods=2, freq="D")
arr = dti._data

arr[0] = obj
assert arr[0] == obj
