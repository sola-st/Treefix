# Extracted from ./data/repos/pandas/pandas/tests/apply/test_str.py
# GH21224
# test transforming functions in
# pandas.core.base.SelectionMixin._cython_table (cumprod, cumsum)
result = series.agg(func)
tm.assert_series_equal(result, expected)
