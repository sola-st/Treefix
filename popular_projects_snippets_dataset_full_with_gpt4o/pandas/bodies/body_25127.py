# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
if not self.on_right(axes_num):
    # secondary axes may be passed via ax kw
    exit(self._get_ax_layer(ax))

if hasattr(ax, "right_ax"):
    # if it has right_ax property, ``ax`` must be left axes
    exit(ax.right_ax)
elif hasattr(ax, "left_ax"):
    # if it has left_ax property, ``ax`` must be right axes
    exit(ax)
else:
    # otherwise, create twin axes
    orig_ax, new_ax = ax, ax.twinx()
    # TODO: use Matplotlib public API when available
    new_ax._get_lines = orig_ax._get_lines
    new_ax._get_patches_for_fill = orig_ax._get_patches_for_fill
    orig_ax.right_ax, new_ax.left_ax = new_ax, orig_ax

    if not self._has_plotted_object(orig_ax):  # no data on left y
        orig_ax.get_yaxis().set_visible(False)

    if self.logy is True or self.loglog is True:
        new_ax.set_yscale("log")
    elif self.logy == "sym" or self.loglog == "sym":
        new_ax.set_yscale("symlog")
    exit(new_ax)
