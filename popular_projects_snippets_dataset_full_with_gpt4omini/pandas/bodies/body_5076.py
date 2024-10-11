# Extracted from ./data/repos/pandas/pandas/tests/scalar/test_nat.py
# see gh-17327
assert NaT.ctime.__doc__ == datetime.ctime.__doc__
