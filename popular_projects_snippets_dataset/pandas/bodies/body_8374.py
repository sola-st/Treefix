# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
timestamp_instance = date_range("2014-03-05", periods=1, freq="D")[0]
ts = Timestamp("2014-03-05")

assert timestamp_instance == ts
