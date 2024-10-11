# Extracted from ./data/repos/pandas/pandas/tests/extension/test_string.py
op_name = f"__{op.__name__}__"
result = getattr(ser, op_name)(other)
expected = getattr(ser.astype(object), op_name)(other).astype("boolean")
self.assert_series_equal(result, expected)
