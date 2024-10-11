# Extracted from ./data/repos/pandas/pandas/tests/series/test_logical_ops.py
# https://github.com/pandas-dev/pandas/pull/23628
# multi-set Index ops are buggy, so let's avoid duplicates...
# GH#49503
ser = Series([True, False])
idx = Index([False, True])

result = op(ser, idx)
tm.assert_series_equal(result, expected)
