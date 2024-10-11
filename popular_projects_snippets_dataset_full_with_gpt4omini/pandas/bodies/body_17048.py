# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
# GH 42800
ser1 = Series([True, False], dtype=dtype1)
ser2 = Series([False, True], dtype=dtype2)
result = concat([ser1, ser2], ignore_index=True)
expected = Series([True, False, False, True], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
