# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# Test properties on Periods with annually frequency.
a_date = Period(freq="A", year=2007)
assert a_date.year == 2007
