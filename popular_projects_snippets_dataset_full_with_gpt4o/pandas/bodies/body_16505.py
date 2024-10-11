# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_crosstab.py
result = crosstab(df["A"], df["C"])
expected = df.groupby(["A", "C"]).size().unstack()
tm.assert_frame_equal(result, expected.fillna(0).astype(np.int64))
