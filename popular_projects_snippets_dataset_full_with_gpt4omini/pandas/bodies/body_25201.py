# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
ax.set_xlim((start_edge, end_edge))

if self.xticks is not None:
    ax.set_xticks(np.array(self.xticks))
else:
    ax.set_xticks(self.tick_pos)
    ax.set_xticklabels(ticklabels)

if name is not None and self.use_index:
    ax.set_xlabel(name)
