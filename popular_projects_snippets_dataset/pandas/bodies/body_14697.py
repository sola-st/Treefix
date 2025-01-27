# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
# test when sharex is set to False, two plots should have different
# labels, GH 25160
df = DataFrame(np.random.rand(10, 2))
df.iloc[5:, 1] = np.nan
df.iloc[:5, 0] = np.nan

figs, axs = self.plt.subplots(2, 1)
df.plot.line(ax=axs, subplots=True, sharex=False)

expected_ax1 = np.arange(4.5, 10, 0.5)
expected_ax2 = np.arange(-0.5, 5, 0.5)

tm.assert_numpy_array_equal(axs[0].get_xticks(), expected_ax1)
tm.assert_numpy_array_equal(axs[1].get_xticks(), expected_ax2)
