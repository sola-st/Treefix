# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# see gh-14404: test the limits of each downcast.
series = to_numeric(Series(min_max), downcast=downcast)
assert series.dtype == dtype
