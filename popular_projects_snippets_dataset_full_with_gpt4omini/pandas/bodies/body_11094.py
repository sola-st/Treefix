# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
grouped = df.groupby(["A", "B"], as_index=False)

# GH #421

result = grouped["C"].agg(len)
expected = grouped.agg(len).loc[:, ["A", "B", "C"]]
tm.assert_frame_equal(result, expected)
