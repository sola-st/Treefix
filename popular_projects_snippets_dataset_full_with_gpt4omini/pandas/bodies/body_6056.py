# Extracted from ./data/repos/pandas/pandas/tests/extension/base/ops.py
if exc is None:
    result = op(ser, other)
    expected = self._combine(ser, other, op)
    assert isinstance(result, type(ser))
    self.assert_equal(result, expected)
else:
    with pytest.raises(exc):
        op(ser, other)
