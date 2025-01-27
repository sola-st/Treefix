# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_misc.py
dti = date_range(freq="BQ-FEB", start=datetime(1998, 1, 1), periods=4)

assert sum(dti.is_quarter_start) == 0
assert sum(dti.is_quarter_end) == 4
assert sum(dti.is_year_start) == 0
assert sum(dti.is_year_end) == 1
