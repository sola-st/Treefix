# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
# GH3254, GH3298 matplotlib/matplotlib#1882, #1892
# regressions in 1.2.1
expected = np.array([0.1, 1.0, 10.0, 100])

# no subplots
df = DataFrame({"A": [3] * 5, "B": list(range(1, 6))}, index=range(5))
ax = df.plot.bar(grid=True, log=True)
tm.assert_numpy_array_equal(ax.yaxis.get_ticklocs(), expected)
