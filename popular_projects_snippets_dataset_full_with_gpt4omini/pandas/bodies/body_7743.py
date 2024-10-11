# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_join.py
# GH29252
df1 = DataFrame(
    data={"col1": [1.1, 1.2]},
    index=MultiIndex.from_product([["A"], [1.0, 2.0]], names=["id1", "id2"]),
)
df2 = DataFrame(
    data={"col2": [2.1, 2.2]},
    index=MultiIndex.from_product([["A"], [np.NaN, 2.0]], names=["id1", "id2"]),
)
result = df1.join(df2)
expected = DataFrame(
    data={"col1": [1.1, 1.2], "col2": [np.nan, 2.2]},
    index=MultiIndex.from_product([["A"], [1.0, 2.0]], names=["id1", "id2"]),
)
tm.assert_frame_equal(result, expected)
