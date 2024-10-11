# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
datetime_instance = datetime(2014, 3, 4)
# build a timestamp with a frequency, since then it supports
# addition/subtraction of integers
timestamp_instance = date_range(datetime_instance, periods=1, freq="D")[0]

ts = Timestamp(datetime_instance)
assert ts == timestamp_instance
