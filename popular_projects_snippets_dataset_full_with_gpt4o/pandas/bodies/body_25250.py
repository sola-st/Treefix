# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/boxplot.py
if self.subplots:
    self._return_obj = pd.Series(dtype=object)

    # Re-create iterated data if `by` is assigned by users
    data = (
        create_iter_data_given_by(self.data, self._kind)
        if self.by is not None
        else self.data
    )

    for i, (label, y) in enumerate(self._iter_data(data=data)):
        ax = self._get_ax(i)
        kwds = self.kwds.copy()

        # When by is applied, show title for subplots to know which group it is
        # just like df.boxplot, and need to apply T on y to provide right input
        if self.by is not None:
            y = y.T
            ax.set_title(pprint_thing(label))

            # When `by` is assigned, the ticklabels will become unique grouped
            # values, instead of label which is used as subtitle in this case.
            ticklabels = [
                pprint_thing(col) for col in self.data.columns.levels[0]
            ]
        else:
            ticklabels = [pprint_thing(label)]

        ret, bp = self._plot(
            ax, y, column_num=i, return_type=self.return_type, **kwds
        )
        self.maybe_color_bp(bp)
        self._return_obj[label] = ret
        self._set_ticklabels(ax, ticklabels)
else:
    y = self.data.values.T
    ax = self._get_ax(0)
    kwds = self.kwds.copy()

    ret, bp = self._plot(
        ax, y, column_num=0, return_type=self.return_type, **kwds
    )
    self.maybe_color_bp(bp)
    self._return_obj = ret

    labels = [left for left, _ in self._iter_data()]
    labels = [pprint_thing(left) for left in labels]
    if not self.use_index:
        labels = [pprint_thing(key) for key in range(len(labels))]
    self._set_ticklabels(ax, labels)
