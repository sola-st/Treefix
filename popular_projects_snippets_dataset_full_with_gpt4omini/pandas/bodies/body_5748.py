# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
result = getattr(s, op_name)(skipna=skipna).astype("Float64")
expected = getattr(s.astype("Float64"), op_name)(skipna=skipna)
self.assert_series_equal(result, expected, check_dtype=False)
