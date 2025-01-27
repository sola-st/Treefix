# Extracted from ./data/repos/pandas/pandas/tests/frame/test_nonunique_indexes.py
# check column dups with index equal and not equal to df's index
df = DataFrame(
    np.random.randn(5, 3),
    index=["a", "b", "c", "d", "e"],
    columns=["A", "B", "A"],
)
for index in [df.index, pd.Index(list("edcba"))]:
    this_df = df.copy()
    expected_ser = Series(index.values, index=this_df.index)
    expected_df = DataFrame(
        {"A": expected_ser, "B": this_df["B"]},
        columns=["A", "B", "A"],
    )
    this_df["A"] = index
    check(this_df, expected_df)
