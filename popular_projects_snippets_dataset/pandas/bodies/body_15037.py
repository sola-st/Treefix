# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
# GH 48884
df = DataFrame(
    [[np.nan, 0.2, 0.3], [0.4, np.nan, np.nan], [0.7, 0.8, 0.9]],
    columns=list("abc"),
)
weights = np.array([0.25, 0.3, 0.45])
no_nan_df = DataFrame([[0.4, 0.2, 0.3], [0.7, 0.8, 0.9]], columns=list("abc"))
no_nan_weights = np.array([[0.3, 0.25, 0.25], [0.45, 0.45, 0.45]])

from matplotlib.patches import Rectangle

_, ax0 = self.plt.subplots()
df.plot.hist(ax=ax0, weights=weights)
rects = [x for x in ax0.get_children() if isinstance(x, Rectangle)]
heights = [rect.get_height() for rect in rects]
_, ax1 = self.plt.subplots()
no_nan_df.plot.hist(ax=ax1, weights=no_nan_weights)
no_nan_rects = [x for x in ax1.get_children() if isinstance(x, Rectangle)]
no_nan_heights = [rect.get_height() for rect in no_nan_rects]
assert all(h0 == h1 for h0, h1 in zip(heights, no_nan_heights))

idxerror_weights = np.array([[0.3, 0.25], [0.45, 0.45]])

msg = "weights must have the same shape as data, or be a single column"
with pytest.raises(ValueError, match=msg):
    _, ax2 = self.plt.subplots()
    no_nan_df.plot.hist(ax=ax2, weights=idxerror_weights)
