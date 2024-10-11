# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
# GH#49974
other = ["1", "2"]

df1 = DataFrame({"x": a, "y": other})
df2 = DataFrame({"x": b, "y": other})

expected = MultiIndex.from_arrays([a, other], names=["x", "y"])

res1 = MultiIndex.from_frame(df1).intersection(
    MultiIndex.from_frame(df2.sort_values(["x", "y"]))
)
res2 = MultiIndex.from_frame(df1).intersection(MultiIndex.from_frame(df2))
res3 = MultiIndex.from_frame(df1.sort_values(["x", "y"])).intersection(
    MultiIndex.from_frame(df2)
)
res4 = MultiIndex.from_frame(df1.sort_values(["x", "y"])).intersection(
    MultiIndex.from_frame(df2.sort_values(["x", "y"]))
)

tm.assert_index_equal(res1, expected)
tm.assert_index_equal(res2, expected)
tm.assert_index_equal(res3, expected)
tm.assert_index_equal(res4, expected)
