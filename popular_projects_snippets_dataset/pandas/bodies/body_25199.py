# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
colors = self._get_colors()
ncolors = len(colors)

pos_prior = neg_prior = np.zeros(len(self.data))
K = self.nseries

for i, (label, y) in enumerate(self._iter_data(fillna=0)):
    ax = self._get_ax(i)
    kwds = self.kwds.copy()
    if self._is_series:
        kwds["color"] = colors
    elif isinstance(colors, dict):
        kwds["color"] = colors[label]
    else:
        kwds["color"] = colors[i % ncolors]

    errors = self._get_errorbars(label=label, index=i)
    kwds = dict(kwds, **errors)

    label = pprint_thing(label)
    label = self._mark_right_label(label, index=i)

    if (("yerr" in kwds) or ("xerr" in kwds)) and (kwds.get("ecolor") is None):
        kwds["ecolor"] = mpl.rcParams["xtick.color"]

    start = 0
    if self.log and (y >= 1).all():
        start = 1
    start = start + self._start_base

    if self.subplots:
        w = self.bar_width / 2
        rect = self._plot(
            ax,
            self.ax_pos + w,
            y,
            self.bar_width,
            start=start,
            label=label,
            log=self.log,
            **kwds,
        )
        ax.set_title(label)
    elif self.stacked:
        mask = y > 0
        start = np.where(mask, pos_prior, neg_prior) + self._start_base
        w = self.bar_width / 2
        rect = self._plot(
            ax,
            self.ax_pos + w,
            y,
            self.bar_width,
            start=start,
            label=label,
            log=self.log,
            **kwds,
        )
        pos_prior = pos_prior + np.where(mask, y, 0)
        neg_prior = neg_prior + np.where(mask, 0, y)
    else:
        w = self.bar_width / K
        rect = self._plot(
            ax,
            self.ax_pos + (i + 0.5) * w,
            y,
            w,
            start=start,
            label=label,
            log=self.log,
            **kwds,
        )
    self._append_legend_handles_labels(rect, label)
