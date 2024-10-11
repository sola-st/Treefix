# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
# GH#36293
mi = MultiIndex.from_arrays([["x", "y", "x"], ["i", "j", "i"]])
df = DataFrame([1, 2, 3], index=mi)
result = df.drop(index="x")
expected = DataFrame([2], index=MultiIndex.from_arrays([["y"], ["j"]]))
tm.assert_frame_equal(result, expected)
