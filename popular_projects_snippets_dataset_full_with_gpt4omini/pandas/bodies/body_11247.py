# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# GH 13901
result = mframe.groupby(level=-1).sum()
expected = mframe.groupby(level="second").sum()
tm.assert_frame_equal(result, expected)

result = mframe.groupby(level=-2).sum()
expected = mframe.groupby(level="first").sum()
tm.assert_frame_equal(result, expected)

result = mframe.groupby(level=[-2, -1]).sum()
expected = mframe.sort_index()
tm.assert_frame_equal(result, expected)

result = mframe.groupby(level=[-1, "first"]).sum()
expected = mframe.groupby(level=["second", "first"]).sum()
tm.assert_frame_equal(result, expected)
