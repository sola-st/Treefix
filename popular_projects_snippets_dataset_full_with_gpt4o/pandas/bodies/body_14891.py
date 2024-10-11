# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# if sum of values is less than 1.0, pie handle them as rate and draw
# semicircle.
series = Series(
    np.random.randint(1, 5), index=["a", "b", "c", "d", "e"], name="YLABEL"
)
ax = _check_plot_works(series.plot.pie)
self._check_text_labels(ax.texts, series.index)
assert ax.get_ylabel() == "YLABEL"

# without wedge labels
ax = _check_plot_works(series.plot.pie, labels=None)
self._check_text_labels(ax.texts, [""] * 5)

# with less colors than elements
color_args = ["r", "g", "b"]
ax = _check_plot_works(series.plot.pie, colors=color_args)

color_expected = ["r", "g", "b", "r", "g"]
self._check_colors(ax.patches, facecolors=color_expected)

# with labels and colors
labels = ["A", "B", "C", "D", "E"]
color_args = ["r", "g", "b", "c", "m"]
ax = _check_plot_works(series.plot.pie, labels=labels, colors=color_args)
self._check_text_labels(ax.texts, labels)
self._check_colors(ax.patches, facecolors=color_args)

# with autopct and fontsize
ax = _check_plot_works(
    series.plot.pie, colors=color_args, autopct="%.2f", fontsize=7
)
pcts = [f"{s*100:.2f}" for s in series.values / series.sum()]
expected_texts = list(chain.from_iterable(zip(series.index, pcts)))
self._check_text_labels(ax.texts, expected_texts)
for t in ax.texts:
    assert t.get_fontsize() == 7

# includes negative value
series = Series([1, 2, 0, 4, -1], index=["a", "b", "c", "d", "e"])
with pytest.raises(ValueError, match="pie plot doesn't allow negative values"):
    series.plot.pie()

# includes nan
series = Series([1, 2, np.nan, 4], index=["a", "b", "c", "d"], name="YLABEL")
ax = _check_plot_works(series.plot.pie)
self._check_text_labels(ax.texts, ["a", "b", "", "d"])
