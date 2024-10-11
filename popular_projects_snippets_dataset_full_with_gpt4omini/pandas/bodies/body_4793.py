# Extracted from ./data/repos/pandas/pandas/tests/strings/test_get_dummies.py
# GH 12180
# Dummies named 'name' should work as expected
s = Series(["a", "b,name", "b"], dtype=any_string_dtype)
result = s.str.get_dummies(",")
expected = DataFrame([[1, 0, 0], [0, 1, 1], [0, 1, 0]], columns=["a", "b", "name"])
tm.assert_frame_equal(result, expected)
