# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH 28652
df = DataFrame({"a": [1, 2]}, index=Index([1, 2]))
result = df.groupby("a").apply(lambda g: g.index)
expected = Series([Index([1]), Index([2])], index=Index([1, 2], name="a"))

tm.assert_series_equal(result, expected)
