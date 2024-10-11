# Extracted from ./data/repos/pandas/pandas/tests/extension/base/ops.py
# divmod has multiple return values, so check separately
if exc is None:
    result_div, result_mod = op(ser, other)
    if op is divmod:
        expected_div, expected_mod = ser // other, ser % other
    else:
        expected_div, expected_mod = other // ser, other % ser
    self.assert_series_equal(result_div, expected_div)
    self.assert_series_equal(result_mod, expected_mod)
else:
    with pytest.raises(exc):
        divmod(ser, other)
