# Extracted from ./data/repos/pandas/pandas/tests/extension/base/ops.py

if op.__name__ in ["eq", "ne"]:
    # comparison should match point-wise comparisons
    result = op(ser, other)
    expected = ser.combine(other, op)
    self.assert_series_equal(result, expected)

else:
    exc = None
    try:
        result = op(ser, other)
    except Exception as err:
        exc = err

    if exc is None:
        # Didn't error, then should match pointwise behavior
        expected = ser.combine(other, op)
        self.assert_series_equal(result, expected)
    else:
        with pytest.raises(type(exc)):
            ser.combine(other, op)
