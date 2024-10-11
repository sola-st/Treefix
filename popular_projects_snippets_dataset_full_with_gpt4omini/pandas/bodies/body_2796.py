# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
df = DataFrame({"x": list(range(5))})
target = np.array([-0.1, 0.9, 1.1, 1.5])

expected = DataFrame({"x": [0, 1, 1, np.nan]}, index=target)
actual = df.reindex(target, method="nearest", tolerance=0.2)
tm.assert_frame_equal(expected, actual)

expected = DataFrame({"x": [0, np.nan, 1, np.nan]}, index=target)
actual = df.reindex(target, method="nearest", tolerance=[0.5, 0.01, 0.4, 0.1])
tm.assert_frame_equal(expected, actual)
