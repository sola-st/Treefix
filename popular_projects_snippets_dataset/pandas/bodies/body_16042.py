# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_tolist.py
# GH49890
ser = Series(values, dtype=dtype)
result_dtype = type(ser.tolist()[0])
assert result_dtype == expected_dtype
