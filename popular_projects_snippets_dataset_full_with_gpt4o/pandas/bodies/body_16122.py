# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
# GH 9910
s = Series(list("abcd"))
# Series of str values should have .str but not .dt/.cat in __dir__
assert "str" in dir(s)
assert "dt" not in dir(s)
assert "cat" not in dir(s)
