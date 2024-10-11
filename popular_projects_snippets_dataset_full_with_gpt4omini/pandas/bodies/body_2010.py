# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# see gh-17007 and gh-17125
#
# Still returns float despite the uint64-nan conflict,
# which would normally force the casting to object.
result = to_numeric(Series(data), errors="coerce")
expected = Series(exp_data, dtype=float)
tm.assert_series_equal(result, expected)
