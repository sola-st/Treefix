# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
indexer = (x for x in [1, 2])
result = df.iloc[indexer, 1]
expected = Series([5, 6], name="b", index=[1, 2])
tm.assert_series_equal(result, expected)
