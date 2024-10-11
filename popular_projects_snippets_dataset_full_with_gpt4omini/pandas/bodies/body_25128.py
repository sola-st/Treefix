# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
if self.subplots:
    naxes = (
        self.nseries if isinstance(self.subplots, bool) else len(self.subplots)
    )
    fig, axes = create_subplots(
        naxes=naxes,
        sharex=self.sharex,
        sharey=self.sharey,
        figsize=self.figsize,
        ax=self.ax,
        layout=self.layout,
        layout_type=self._layout_type,
    )
else:
    if self.ax is None:
        fig = self.plt.figure(figsize=self.figsize)
        axes = fig.add_subplot(111)
    else:
        fig = self.ax.get_figure()
        if self.figsize is not None:
            fig.set_size_inches(self.figsize)
        axes = self.ax

axes = flatten_axes(axes)

valid_log = {False, True, "sym", None}
input_log = {self.logx, self.logy, self.loglog}
if input_log - valid_log:
    invalid_log = next(iter(input_log - valid_log))
    raise ValueError(
        f"Boolean, None and 'sym' are valid options, '{invalid_log}' is given."
    )

if self.logx is True or self.loglog is True:
    [a.set_xscale("log") for a in axes]
elif self.logx == "sym" or self.loglog == "sym":
    [a.set_xscale("symlog") for a in axes]

if self.logy is True or self.loglog is True:
    [a.set_yscale("log") for a in axes]
elif self.logy == "sym" or self.loglog == "sym":
    [a.set_yscale("symlog") for a in axes]

self.fig = fig
self.axes = axes
