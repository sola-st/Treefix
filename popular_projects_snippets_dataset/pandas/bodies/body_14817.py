# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# Test if multiindex plot index have a fixed xtick position
# GH: 15912
index = MultiIndex.from_product([[2012, 2013], [1, 2]])
df = DataFrame(np.random.randn(4, 2), columns=["A", "B"], index=index)
ax = df.plot()
ax.set_xlim(-1, 4)
xticklabels = [t.get_text() for t in ax.get_xticklabels()]
labels_position = dict(zip(xticklabels, ax.get_xticks()))
# Testing if the label stayed at the right position
assert labels_position["(2012, 1)"] == 0.0
assert labels_position["(2012, 2)"] == 1.0
assert labels_position["(2013, 1)"] == 2.0
assert labels_position["(2013, 2)"] == 3.0
