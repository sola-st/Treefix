# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
df = DataFrame([[1, 2, 3, 4], [5, 6, 7, 8]], columns=["A", "B", "C", "D"])

# With MultiIndex
result = df.set_index(["A", "B"]).reset_index(level=levels[0])
tm.assert_frame_equal(result, df.set_index("B"))

result = df.set_index(["A", "B"]).reset_index(level=levels[:1])
tm.assert_frame_equal(result, df.set_index("B"))

result = df.set_index(["A", "B"]).reset_index(level=levels)
tm.assert_frame_equal(result, df)

result = df.set_index(["A", "B"]).reset_index(level=levels, drop=True)
tm.assert_frame_equal(result, df[["C", "D"]])

# With single-level Index (GH 16263)
result = df.set_index("A").reset_index(level=levels[0])
tm.assert_frame_equal(result, df)

result = df.set_index("A").reset_index(level=levels[:1])
tm.assert_frame_equal(result, df)

result = df.set_index(["A"]).reset_index(level=levels[0], drop=True)
tm.assert_frame_equal(result, df[["B", "C", "D"]])
