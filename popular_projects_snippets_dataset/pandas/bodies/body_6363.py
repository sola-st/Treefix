# Extracted from ./data/repos/pandas/pandas/tests/extension/test_boolean.py
if exc is None:
    if op_name in self.implements:
        msg = r"numpy boolean subtract"
        with pytest.raises(TypeError, match=msg):
            op(obj, other)
        exit()

    result = op(obj, other)
    expected = self._combine(obj, other, op)

    if op_name in (
        "__floordiv__",
        "__rfloordiv__",
        "__pow__",
        "__rpow__",
        "__mod__",
        "__rmod__",
    ):
        # combine keeps boolean type
        expected = expected.astype("Int8")
    elif op_name in ("__truediv__", "__rtruediv__"):
        # combine with bools does not generate the correct result
        #  (numpy behaviour for div is to regard the bools as numeric)
        expected = self._combine(obj.astype(float), other, op)
        expected = expected.astype("Float64")
    if op_name == "__rpow__":
        # for rpow, combine does not propagate NaN
        expected[result.isna()] = np.nan
    self.assert_equal(result, expected)
else:
    with pytest.raises(exc):
        op(obj, other)
