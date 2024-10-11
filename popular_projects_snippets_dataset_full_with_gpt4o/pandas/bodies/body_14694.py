# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
expected = np.array([0.1, 1.0, 10.0, 100.0, 1000.0, 1e4])

ax = DataFrame([Series([200, 300]), Series([300, 500])]).plot.bar(
    log=True, subplots=True
)

tm.assert_numpy_array_equal(ax[0].yaxis.get_ticklocs(), expected)
tm.assert_numpy_array_equal(ax[1].yaxis.get_ticklocs(), expected)
