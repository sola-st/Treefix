# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_common.py
fig = self.plt.gcf()
gen = _gen_two_subplots(f=lambda **kwargs: None, fig=fig, ax="test")
# On the first yield, no subplot should be added since ax was passed
next(gen)
assert fig.get_axes() == []
# On the second, the one axis should match fig.subplot(2, 1, 2)
next(gen)
axes = fig.get_axes()
assert len(axes) == 1
subplot_geometry = list(axes[0].get_subplotspec().get_geometry()[:-1])
subplot_geometry[-1] += 1
assert subplot_geometry == [2, 1, 2]
