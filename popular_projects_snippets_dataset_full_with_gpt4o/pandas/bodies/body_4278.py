# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH34388
df1 = DataFrame({"A": [0, 1, 2], "B": [1, 2, 3]})
df1.columns = df1.columns.set_names("L1")

df2 = DataFrame({("A", "C"): [0, 0, 0], ("A", "D"): [0, 0, 0]})
df2.columns = df2.columns.set_names(["L1", "L2"])

result = df1.add(df2, level=level)
expected = DataFrame({("A", "C"): [0, 1, 2], ("A", "D"): [0, 1, 2]})
expected.columns = expected.columns.set_names(["L1", "L2"])

tm.assert_frame_equal(result, expected)
