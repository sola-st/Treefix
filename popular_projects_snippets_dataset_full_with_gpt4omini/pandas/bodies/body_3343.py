# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH-41333, GH-35977
dtype = any_string_dtype
obj = frame_or_series(data, dtype=dtype)
result = obj.replace(to_replace, regex=True)
expected = frame_or_series(expected, dtype=dtype)

tm.assert_equal(result, expected)
