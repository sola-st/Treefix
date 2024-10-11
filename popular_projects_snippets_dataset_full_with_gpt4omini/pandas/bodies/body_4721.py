# Extracted from ./data/repos/pandas/pandas/tests/strings/test_extract.py
s = Series(["a3", "b3", "c2"], name="bob", dtype=any_string_dtype)
result = s.str.extract(r"(?P<sue>[a-z])", expand=False)
expected = Series(["a", "b", "c"], name="sue", dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
