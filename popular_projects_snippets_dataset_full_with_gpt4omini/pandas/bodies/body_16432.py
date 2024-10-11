# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
# see gh-1979
result = tmod._round_frac(val, precision=precision)
assert result == expected
