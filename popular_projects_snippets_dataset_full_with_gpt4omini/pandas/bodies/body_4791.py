# Extracted from ./data/repos/pandas/pandas/tests/strings/test_get_dummies.py
s = Series(["a|b", "a|c", np.nan], dtype=any_string_dtype)
result = s.str.get_dummies("|")
expected = DataFrame([[1, 1, 0], [1, 0, 1], [0, 0, 0]], columns=list("abc"))
tm.assert_frame_equal(result, expected)

s = Series(["a;b", "a", 7], dtype=any_string_dtype)
result = s.str.get_dummies(";")
expected = DataFrame([[0, 1, 1], [0, 1, 0], [1, 0, 0]], columns=list("7ab"))
tm.assert_frame_equal(result, expected)
