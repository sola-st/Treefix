# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
frame = DataFrame(
    [[1, 1, 2], [3, 1, 0], [4, 5, 6]], index=[1, 2, 3], columns=list("ABC")
)

# by column (axis=0)
sorted_df = frame.sort_values(by="A")
indexer = frame["A"].argsort().values
expected = frame.loc[frame.index[indexer]]
tm.assert_frame_equal(sorted_df, expected)

sorted_df = frame.sort_values(by="A", ascending=False)
indexer = indexer[::-1]
expected = frame.loc[frame.index[indexer]]
tm.assert_frame_equal(sorted_df, expected)

sorted_df = frame.sort_values(by="A", ascending=False)
tm.assert_frame_equal(sorted_df, expected)

# GH4839
sorted_df = frame.sort_values(by=["A"], ascending=[False])
tm.assert_frame_equal(sorted_df, expected)

# multiple bys
sorted_df = frame.sort_values(by=["B", "C"])
expected = frame.loc[[2, 1, 3]]
tm.assert_frame_equal(sorted_df, expected)

sorted_df = frame.sort_values(by=["B", "C"], ascending=False)
tm.assert_frame_equal(sorted_df, expected[::-1])

sorted_df = frame.sort_values(by=["B", "A"], ascending=[True, False])
tm.assert_frame_equal(sorted_df, expected)

msg = "No axis named 2 for object type DataFrame"
with pytest.raises(ValueError, match=msg):
    frame.sort_values(by=["A", "B"], axis=2, inplace=True)

# by row (axis=1): GH#10806
sorted_df = frame.sort_values(by=3, axis=1)
expected = frame
tm.assert_frame_equal(sorted_df, expected)

sorted_df = frame.sort_values(by=3, axis=1, ascending=False)
expected = frame.reindex(columns=["C", "B", "A"])
tm.assert_frame_equal(sorted_df, expected)

sorted_df = frame.sort_values(by=[1, 2], axis="columns")
expected = frame.reindex(columns=["B", "A", "C"])
tm.assert_frame_equal(sorted_df, expected)

sorted_df = frame.sort_values(by=[1, 3], axis=1, ascending=[True, False])
tm.assert_frame_equal(sorted_df, expected)

sorted_df = frame.sort_values(by=[1, 3], axis=1, ascending=False)
expected = frame.reindex(columns=["C", "B", "A"])
tm.assert_frame_equal(sorted_df, expected)

msg = r"Length of ascending \(5\) != length of by \(2\)"
with pytest.raises(ValueError, match=msg):
    frame.sort_values(by=["A", "B"], axis=0, ascending=[True] * 5)
