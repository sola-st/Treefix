# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
"""Common post process unrelated to data"""
if len(self.axes) > 0:
    all_axes = self._get_subplots()
    nrows, ncols = self._get_axes_layout()
    handle_shared_axes(
        axarr=all_axes,
        nplots=len(all_axes),
        naxes=nrows * ncols,
        nrows=nrows,
        ncols=ncols,
        sharex=self.sharex,
        sharey=self.sharey,
    )

for ax in self.axes:
    ax = getattr(ax, "right_ax", ax)
    if self.yticks is not None:
        ax.set_yticks(self.yticks)

    if self.xticks is not None:
        ax.set_xticks(self.xticks)

    if self.ylim is not None:
        ax.set_ylim(self.ylim)

    if self.xlim is not None:
        ax.set_xlim(self.xlim)

    # GH9093, currently Pandas does not show ylabel, so if users provide
    # ylabel will set it as ylabel in the plot.
    if self.ylabel is not None:
        ax.set_ylabel(pprint_thing(self.ylabel))

    ax.grid(self.grid)

if self.title:
    if self.subplots:
        if is_list_like(self.title):
            if len(self.title) != self.nseries:
                raise ValueError(
                    "The length of `title` must equal the number "
                    "of columns if using `title` of type `list` "
                    "and `subplots=True`.\n"
                    f"length of title = {len(self.title)}\n"
                    f"number of columns = {self.nseries}"
                )

            for (ax, title) in zip(self.axes, self.title):
                ax.set_title(title)
        else:
            self.fig.suptitle(self.title)
    else:
        if is_list_like(self.title):
            msg = (
                "Using `title` of type `list` is not supported "
                "unless `subplots=True` is passed"
            )
            raise ValueError(msg)
        self.axes[0].set_title(self.title)
