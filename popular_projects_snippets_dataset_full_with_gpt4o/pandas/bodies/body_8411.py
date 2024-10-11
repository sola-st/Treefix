# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH 6961
dr = date_range("2014", "2015", freq="M")
assert dr[0] == datetime(2014, 1, 31)
assert dr[-1] == datetime(2014, 12, 31)
