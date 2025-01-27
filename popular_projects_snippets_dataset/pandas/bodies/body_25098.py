# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/hist.py
ax.hist(group.dropna().values, bins=bins, **kwargs)
if legend:
    ax.legend()
