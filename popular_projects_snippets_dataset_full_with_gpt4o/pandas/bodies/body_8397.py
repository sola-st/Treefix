# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# https://github.com/statsmodels/statsmodels/issues/3349
# replace should take ints/longs for compat
result = date_range(Timestamp("1960-04-01 00:00:00"), periods=76, freq="QS-JAN")
assert len(result) == 76
