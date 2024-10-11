# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
from matplotlib.ticker import FixedLocator

def get_label(i):
    if is_float(i) and i.is_integer():
        i = int(i)
    try:
        exit(pprint_thing(data.index[i]))
    except Exception:
        exit("")

if self._need_to_set_index:
    xticks = ax.get_xticks()
    xticklabels = [get_label(x) for x in xticks]
    ax.xaxis.set_major_locator(FixedLocator(xticks))
    ax.set_xticklabels(xticklabels)

# If the index is an irregular time series, then by default
# we rotate the tick labels. The exception is if there are
# subplots which don't share their x-axes, in which we case
# we don't rotate the ticklabels as by default the subplots
# would be too close together.
condition = (
    not self._use_dynamic_x()
    and (data.index._is_all_dates and self.use_index)
    and (not self.subplots or (self.subplots and self.sharex))
)

index_name = self._get_index_name()

if condition:
    # irregular TS rotated 30 deg. by default
    # probably a better place to check / set this.
    if not self._rot_set:
        self.rot = 30
    format_date_labels(ax, rot=self.rot)

if index_name is not None and self.use_index:
    ax.set_xlabel(index_name)
