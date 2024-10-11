# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
# GH#41575
df = DataFrame([[1, 2, 3]], columns=["A", "B", "C"], dtype=dtype)
df["B"] = df["B"].astype(int)
df["C"] = df["C"].astype(float)

result = df.iloc[:0].groupby("A").describe(**kwargs)
expected = df.groupby("A").describe(**kwargs).reset_index(drop=True).iloc[:0]
tm.assert_frame_equal(result, expected)

result = df.iloc[:0].groupby("A").B.describe(**kwargs)
expected = df.groupby("A").B.describe(**kwargs).reset_index(drop=True).iloc[:0]
expected.index = Index([])
tm.assert_frame_equal(result, expected)
