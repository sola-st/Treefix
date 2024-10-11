# Extracted from ./data/repos/pandas/pandas/tests/extension/test_integer.py
if exc is None:
    sdtype = tm.get_dtype(s)

    if (
        hasattr(other, "dtype")
        and not is_extension_array_dtype(other.dtype)
        and is_integer_dtype(other.dtype)
        and sdtype.is_unsigned_integer
    ):
        # TODO: comment below is inaccurate; other can be int8, int16, ...
        #  and the trouble is that e.g. if s is UInt8 and other is int8,
        #  then result is UInt16
        # other is np.int64 and would therefore always result in
        # upcasting, so keeping other as same numpy_dtype
        other = other.astype(sdtype.numpy_dtype)

    result = op(s, other)
    expected = self._combine(s, other, op)

    if op_name in ("__rtruediv__", "__truediv__", "__div__"):
        expected = expected.fillna(np.nan).astype("Float64")
    else:
        # combine method result in 'biggest' (int64) dtype
        expected = expected.astype(sdtype)

    self.assert_equal(result, expected)
else:
    with pytest.raises(exc):
        op(s, other)
