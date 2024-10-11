# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# #1645
rng = date_range("1/1/2000", periods=10, freq="BMS")

ex_first = Timestamp("2000-01-03")
assert rng[0] == ex_first
