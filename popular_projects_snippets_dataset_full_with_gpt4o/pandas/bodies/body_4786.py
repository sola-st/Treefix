# Extracted from ./data/repos/pandas/pandas/tests/strings/test_api.py

# GH 6106, GH 9322
assert Series.str is strings.StringMethods
assert isinstance(Series([""], dtype=any_string_dtype).str, strings.StringMethods)
