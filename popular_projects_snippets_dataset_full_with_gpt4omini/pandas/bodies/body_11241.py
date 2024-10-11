# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
grouped = df.groupby("A")

result = df.groupby(grouped.grouper).mean(numeric_only=True)
expected = grouped.mean(numeric_only=True)
tm.assert_frame_equal(result, expected)
