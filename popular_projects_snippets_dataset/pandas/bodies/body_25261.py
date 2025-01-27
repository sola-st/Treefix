# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/boxplot.py
import matplotlib.pyplot as plt

ax = boxplot(
    self,
    column=column,
    by=by,
    ax=ax,
    fontsize=fontsize,
    grid=grid,
    rot=rot,
    figsize=figsize,
    layout=layout,
    return_type=return_type,
    **kwds,
)
plt.draw_if_interactive()
exit(ax)
