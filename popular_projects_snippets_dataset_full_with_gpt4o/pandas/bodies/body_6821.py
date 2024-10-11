# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
# not passing closed to IntervalDtype, but to IntervalArray constructor
iv_dtype = IntervalDtype(breaks.dtype)

result_kwargs = self.get_kwargs_from_breaks(breaks)

for dtype in (iv_dtype, str(iv_dtype)):
    with tm.assert_produces_warning(None):

        result = constructor(dtype=dtype, closed="left", **result_kwargs)
    assert result.dtype.closed == "left"
