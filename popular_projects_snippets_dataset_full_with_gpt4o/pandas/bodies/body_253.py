# Extracted from ./data/repos/pandas/pandas/tests/apply/test_str.py
# GH 21224
# test transforming functions in
# pandas.core.base.SelectionMixin._cython_table (cumprod, cumsum)
if axis in ("columns", 1):
    # operating blockwise doesn't let us preserve dtypes
    expected = expected.astype("float64")

result = df.agg(func, axis=axis)
tm.assert_frame_equal(result, expected)
