# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_explode.py
s = pd.Series([[0, 1, 2], np.nan, [], (3, 4)], index=list("abcd"), name="foo")
result = s.explode()
expected = pd.Series(
    [0, 1, 2, np.nan, np.nan, 3, 4], index=list("aaabcdd"), dtype=object, name="foo"
)
tm.assert_series_equal(result, expected)
