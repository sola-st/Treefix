# Extracted from ./data/repos/pandas/pandas/tests/extension/test_floating.py
if exc is None:
    sdtype = tm.get_dtype(s)
    if (
        hasattr(other, "dtype")
        and not is_extension_array_dtype(other.dtype)
        and is_float_dtype(other.dtype)
    ):
        # other is np.float64 and would therefore always result in
        # upcasting, so keeping other as same numpy_dtype
        other = other.astype(sdtype.numpy_dtype)

    result = op(s, other)
    expected = self._combine(s, other, op)

    # combine method result in 'biggest' (float64) dtype
    expected = expected.astype(sdtype)

    self.assert_equal(result, expected)
else:
    with pytest.raises(exc):
        op(s, other)
