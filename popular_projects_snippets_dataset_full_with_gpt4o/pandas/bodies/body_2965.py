# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
# GH#10907
df = DataFrame({"y": Series([2]), "z": Series([3])})
df.insert(0, "x", 1)
result = df.diff(axis=1)
expected = DataFrame({"x": np.nan, "y": Series(1), "z": Series(1)})
tm.assert_frame_equal(result, expected)
