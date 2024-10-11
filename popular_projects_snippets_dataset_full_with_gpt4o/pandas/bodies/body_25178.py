# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
if self._is_ts_plot():
    data = maybe_convert_index(self._get_ax(0), self.data)

    x = data.index  # dummy, not used
    plotf = self._ts_plot
    it = self._iter_data(data=data, keep_index=True)
else:
    x = self._get_xticks(convert_period=True)
    # error: Incompatible types in assignment (expression has type
    # "Callable[[Any, Any, Any, Any, Any, Any, KwArg(Any)], Any]", variable has
    # type "Callable[[Any, Any, Any, Any, KwArg(Any)], Any]")
    plotf = self._plot  # type: ignore[assignment]
    it = self._iter_data()

stacking_id = self._get_stacking_id()
is_errorbar = com.any_not_none(*self.errors.values())

colors = self._get_colors()
for i, (label, y) in enumerate(it):
    ax = self._get_ax(i)
    kwds = self.kwds.copy()
    style, kwds = self._apply_style_colors(colors, kwds, i, label)

    errors = self._get_errorbars(label=label, index=i)
    kwds = dict(kwds, **errors)

    label = pprint_thing(label)  # .encode('utf-8')
    label = self._mark_right_label(label, index=i)
    kwds["label"] = label

    newlines = plotf(
        ax,
        x,
        y,
        style=style,
        column_num=i,
        stacking_id=stacking_id,
        is_errorbar=is_errorbar,
        **kwds,
    )
    self._append_legend_handles_labels(newlines[0], label)

    if self._is_ts_plot():

        # reset of xlim should be used for ts data
        # TODO: GH28021, should find a way to change view limit on xaxis
        lines = get_all_lines(ax)
        left, right = get_xlim(lines)
        ax.set_xlim(left, right)
