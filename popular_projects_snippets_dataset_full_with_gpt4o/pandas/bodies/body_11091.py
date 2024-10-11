# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
grouped = df.groupby("A", as_index=False)
grouped2 = df.groupby(["A", "B"], as_index=False)

result = grouped["C"].agg(np.sum)
expected = grouped.agg(np.sum).loc[:, ["A", "C"]]
assert isinstance(result, DataFrame)
tm.assert_frame_equal(result, expected)

result2 = grouped2["C"].agg(np.sum)
expected2 = grouped2.agg(np.sum).loc[:, ["A", "B", "C"]]
assert isinstance(result2, DataFrame)
tm.assert_frame_equal(result2, expected2)

result = grouped["C"].sum()
expected = grouped.sum().loc[:, ["A", "C"]]
assert isinstance(result, DataFrame)
tm.assert_frame_equal(result, expected)

result2 = grouped2["C"].sum()
expected2 = grouped2.sum().loc[:, ["A", "B", "C"]]
assert isinstance(result2, DataFrame)
tm.assert_frame_equal(result2, expected2)
