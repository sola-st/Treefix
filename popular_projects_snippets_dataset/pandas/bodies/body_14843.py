# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_color.py
# addressing issue #10678, to ensure colobar does not
# interfere with x-axis label and ticklabels with
# ipython inline backend.
random_array = np.random.random((1000, 3))
df = DataFrame(random_array, columns=["A label", "B label", "C label"])

ax = df.plot.hexbin("A label", "B label", gridsize=12)
assert all(vis.get_visible() for vis in ax.xaxis.get_minorticklabels())
assert all(vis.get_visible() for vis in ax.xaxis.get_majorticklabels())
assert ax.xaxis.get_label().get_visible()
