# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#47867 all steps are necessary to reproduce the initial bug
df = DataFrame(
    {"bool_col": True, "a": 1, "b": 2.5},
    index=MultiIndex.from_arrays([[1, 2], [1, 2]], names=["idx1", "idx2"]),
)
idx = [(1, 1)]

df["c"] = 3
df.loc[idx, "c"] = 0

df.loc[idx, "c"]
df.loc[idx, ["a", "b"]]

df.loc[idx, "c"] = 15
result = df.loc[idx, "c"]
expected = df = Series(
    15,
    index=MultiIndex.from_arrays([[1], [1]], names=["idx1", "idx2"]),
    name="c",
)
tm.assert_series_equal(result, expected)
