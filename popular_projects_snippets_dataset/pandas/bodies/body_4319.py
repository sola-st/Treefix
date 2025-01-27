# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
index = ["A", "B", "C"]
columns = ["X", "Y", "Z"]
df = DataFrame(np.random.randn(3, 3), index=index, columns=columns)

align = pd.core.ops.align_method_FRAME

expected = DataFrame({"X": val, "Y": val, "Z": val}, index=df.index)
tm.assert_frame_equal(align(df, val, "index")[1], expected)

expected = DataFrame(
    {"X": [1, 1, 1], "Y": [2, 2, 2], "Z": [3, 3, 3]}, index=df.index
)
tm.assert_frame_equal(align(df, val, "columns")[1], expected)
