# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py

cat1 = Categorical(
    ["a", "a", "b", "b"], categories=["a", "b", "z"], ordered=True
)
cat2 = Categorical(
    ["c", "d", "c", "d"], categories=["c", "d", "y"], ordered=True
)
df = DataFrame({"A": cat1, "B": cat2, "values": [1, 2, 3, 4]})
result = pivot_table(df, values="values", index=["A", "B"], dropna=True)

exp_index = MultiIndex.from_arrays([cat1, cat2], names=["A", "B"])
expected = DataFrame({"values": [1, 2, 3, 4]}, index=exp_index)
tm.assert_frame_equal(result, expected)
