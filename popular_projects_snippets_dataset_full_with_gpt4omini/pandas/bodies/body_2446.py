# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# See gh-12218
mi = MultiIndex.from_product([["x", "y"], [0, 1]], names=[None, "c"])
dg = DataFrame(
    [[1, 1, 2, 2], [3, 3, 4, 4]], columns=mi, index=Index([0, 1], name="i")
)
with pytest.raises(InvalidIndexError, match="slice"):
    dg[:, 0]

index = Index(range(2), name="i")
columns = MultiIndex(
    levels=[["x", "y"], [0, 1]], codes=[[0, 1], [0, 0]], names=[None, "c"]
)
expected = DataFrame([[1, 2], [3, 4]], columns=columns, index=index)

result = dg.loc[:, (slice(None), 0)]
tm.assert_frame_equal(result, expected)

name = ("x", 0)
index = Index(range(2), name="i")
expected = Series([1, 3], index=index, name=name)

result = dg["x", 0]
tm.assert_series_equal(result, expected)
