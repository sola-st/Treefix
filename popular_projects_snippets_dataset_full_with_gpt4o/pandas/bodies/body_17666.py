# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_year.py
offset = BYearEnd(month=6)
date = datetime(2009, 11, 30)

assert offset.rollforward(date) == datetime(2010, 6, 30)
assert offset.rollback(date) == datetime(2009, 6, 30)
