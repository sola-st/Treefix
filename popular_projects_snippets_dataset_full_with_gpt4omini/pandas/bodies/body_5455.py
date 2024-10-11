# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
assert ts.is_year_start
assert ts.is_quarter_start
assert ts.is_month_start
assert not ts.is_year_end
assert not ts.is_month_end
assert not ts.is_month_end

# 2016-01-01 is a Friday, so is year/quarter/month start with this freq
assert ts.is_year_start
assert ts.is_quarter_start
assert ts.is_month_start
assert not ts.is_year_end
assert not ts.is_month_end
assert not ts.is_month_end
