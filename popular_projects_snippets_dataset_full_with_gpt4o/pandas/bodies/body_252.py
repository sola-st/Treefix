# Extracted from ./data/repos/pandas/pandas/tests/apply/test_str.py
# GH 21224
# test reducing functions in
# pandas.core.base.SelectionMixin._cython_table
result = df.agg(func, axis=axis)
tm.assert_series_equal(result, expected)
