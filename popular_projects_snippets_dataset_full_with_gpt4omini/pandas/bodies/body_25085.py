# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/hist.py
colors = self._get_colors()
stacking_id = self._get_stacking_id()

# Re-create iterated data if `by` is assigned by users
data = (
    create_iter_data_given_by(self.data, self._kind)
    if self.by is not None
    else self.data
)

for i, (label, y) in enumerate(self._iter_data(data=data)):
    ax = self._get_ax(i)

    kwds = self.kwds.copy()

    label = pprint_thing(label)
    label = self._mark_right_label(label, index=i)
    kwds["label"] = label

    style, kwds = self._apply_style_colors(colors, kwds, i, label)
    if style is not None:
        kwds["style"] = style

    kwds = self._make_plot_keywords(kwds, y)

    # the bins is multi-dimension array now and each plot need only 1-d and
    # when by is applied, label should be columns that are grouped
    if self.by is not None:
        kwds["bins"] = kwds["bins"][i]
        kwds["label"] = self.columns
        kwds.pop("color")

    # We allow weights to be a multi-dimensional array, e.g. a (10, 2) array,
    # and each sub-array (10,) will be called in each iteration. If users only
    # provide 1D array, we assume the same weights is used for all iterations
    weights = kwds.get("weights", None)
    if weights is not None:
        if np.ndim(weights) != 1 and np.shape(weights)[-1] != 1:
            try:
                weights = weights[:, i]
            except IndexError as err:
                raise ValueError(
                    "weights must have the same shape as data, "
                    "or be a single column"
                ) from err
        weights = weights[~isna(y)]
        kwds["weights"] = weights

    y = reformat_hist_y_given_by(y, self.by)

    artists = self._plot(ax, y, column_num=i, stacking_id=stacking_id, **kwds)

    # when by is applied, show title for subplots to know which group it is
    if self.by is not None:
        ax.set_title(pprint_thing(label))

    self._append_legend_handles_labels(artists[0], label)
