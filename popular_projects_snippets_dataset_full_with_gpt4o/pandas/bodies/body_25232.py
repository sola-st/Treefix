# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/tools.py
# mini version of autofmt_xdate
for label in ax.get_xticklabels():
    label.set_ha("right")
    label.set_rotation(rot)
fig = ax.get_figure()
maybe_adjust_figure(fig, bottom=0.2)
