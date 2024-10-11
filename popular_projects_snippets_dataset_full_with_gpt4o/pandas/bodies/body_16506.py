# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
result = crosstab(df["A"], [df["B"], df["C"]])
expected = df.groupby(["A", "B", "C"]).size()
expected = expected.unstack("B").unstack("C").fillna(0).astype(np.int64)
tm.assert_frame_equal(result, expected)

result = crosstab([df["B"], df["C"]], df["A"])
expected = df.groupby(["B", "C", "A"]).size()
expected = expected.unstack("A").fillna(0).astype(np.int64)
tm.assert_frame_equal(result, expected)
