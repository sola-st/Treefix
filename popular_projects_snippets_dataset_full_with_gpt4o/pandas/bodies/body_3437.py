# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
idx = IntervalIndex.from_breaks(np.arange(11), name="x")
original = DataFrame({"x": idx, "y": np.arange(10)})[["x", "y"]]

result = original.set_index("x")
expected = DataFrame({"y": np.arange(10)}, index=idx)
tm.assert_frame_equal(result, expected)

result2 = result.reset_index()
tm.assert_frame_equal(result2, original)
