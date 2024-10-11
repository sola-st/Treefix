# Extracted from ./data/repos/pandas/pandas/tests/strings/test_case_justify.py
s = Series(["1", "22", "aaa", "333", "45678"], dtype=any_string_dtype)

result = s.str.zfill(5)
expected = Series(
    ["00001", "00022", "00aaa", "00333", "45678"], dtype=any_string_dtype
)
tm.assert_series_equal(result, expected)
expected = np.array([v.zfill(5) for v in np.array(s)], dtype=np.object_)
tm.assert_numpy_array_equal(np.array(result, dtype=np.object_), expected)

result = s.str.zfill(3)
expected = Series(["001", "022", "aaa", "333", "45678"], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
expected = np.array([v.zfill(3) for v in np.array(s)], dtype=np.object_)
tm.assert_numpy_array_equal(np.array(result, dtype=np.object_), expected)

s = Series(["1", np.nan, "aaa", np.nan, "45678"], dtype=any_string_dtype)
result = s.str.zfill(5)
expected = Series(
    ["00001", np.nan, "00aaa", np.nan, "45678"], dtype=any_string_dtype
)
tm.assert_series_equal(result, expected)
