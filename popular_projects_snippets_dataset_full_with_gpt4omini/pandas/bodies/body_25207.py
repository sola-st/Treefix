# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
# horizontal bars
ax.set_ylim((start_edge, end_edge))
ax.set_yticks(self.tick_pos)
ax.set_yticklabels(ticklabels)
if name is not None and self.use_index:
    ax.set_ylabel(name)
ax.set_xlabel(self.xlabel)
