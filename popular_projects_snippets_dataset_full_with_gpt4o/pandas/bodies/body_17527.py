# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_month.py
dt = datetime(2007, 1, 1, 3)

result = dt + BMonthEnd(normalize=True)
expected = dt.replace(hour=0) + BMonthEnd()
assert result == expected
