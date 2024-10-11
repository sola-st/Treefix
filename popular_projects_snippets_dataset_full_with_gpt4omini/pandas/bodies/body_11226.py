# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
result = df.groupby("A").C.sum()
expected = df.groupby("A")["C"].sum()
tm.assert_series_equal(result, expected)

df["mean"] = 1.5
result = df.groupby("A").mean(numeric_only=True)
expected = df.groupby("A")[["C", "D", "mean"]].agg(np.mean)
tm.assert_frame_equal(result, expected)
