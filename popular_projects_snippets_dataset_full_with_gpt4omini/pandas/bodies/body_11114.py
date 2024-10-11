# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
grouped = df.groupby(df["A"].values)
result = grouped.sum()
expected = df.groupby(df["A"].rename(None)).sum()
tm.assert_frame_equal(result, expected)
