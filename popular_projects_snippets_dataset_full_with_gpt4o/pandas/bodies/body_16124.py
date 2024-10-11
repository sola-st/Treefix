# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
# Similarly for .cat, but with the twist that str and dt should be
# there if the categories are of that type first cat and str.
s = Series(list("abbcd"), dtype="category")
assert "cat" in dir(s)
assert "str" in dir(s)  # as it is a string categorical
assert "dt" not in dir(s)
