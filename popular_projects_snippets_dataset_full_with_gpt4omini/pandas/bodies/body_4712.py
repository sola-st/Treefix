# Extracted from ./data/repos/pandas/pandas/tests/strings/test_string_array.py
# https://github.com/pandas-dev/pandas/issues/30969
# Only expand=False & multiple groups was failing

a = Series(["a1", "b2", "cc"], dtype=nullable_string_dtype)
b = Series(["a1", "b2", "cc"], dtype="object")
pat = r"(\w)(\d)"

result = a.str.extract(pat, expand=False)
expected = b.str.extract(pat, expand=False)
assert all(result.dtypes == nullable_string_dtype)

result = result.astype(object)
tm.assert_equal(result, expected)
