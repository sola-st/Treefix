# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
# GH 12979
df = DataFrame(np.random.randn(5, 5))
ax = df.plot.bar(stacked=True, width=w)
ticks = ax.xaxis.get_ticklocs()
tm.assert_numpy_array_equal(ticks, np.array([0, 1, 2, 3, 4]))
assert ax.get_xlim() == (-0.75, 4.75)
# check left-edge of bars
assert ax.patches[0].get_x() == -0.5
assert ax.patches[-1].get_x() == 3.5
