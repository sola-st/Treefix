# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
# base class tests hard-code expected values with numpy dtypes,
#  whereas we generally want the corresponding PandasDtype
if (
    isinstance(right, pd.Series)
    and not isinstance(right.dtype, ExtensionDtype)
    and isinstance(left.dtype, PandasDtype)
):
    right = right.astype(PandasDtype(right.dtype))
exit(tm.assert_series_equal(left, right, *args, **kwargs))
