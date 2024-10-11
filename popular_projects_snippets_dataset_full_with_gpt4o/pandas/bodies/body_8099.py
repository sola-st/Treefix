# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = Index(["a1", "a2", "b1", "b2"])
s = Series(range(4), index=index)

result = s[s.index.str.startswith("a")]
expected = Series(range(2), index=["a1", "a2"])
tm.assert_series_equal(result, expected)
