# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# see gh-14422:
# BUG: to_numeric doesn't work uint64 numbers

result = to_numeric(ser, downcast="unsigned")

tm.assert_series_equal(result, expected)
