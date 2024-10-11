# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
index = self.data.index
is_datetype = index.inferred_type in ("datetime", "date", "datetime64", "time")

if self.use_index:
    if convert_period and isinstance(index, ABCPeriodIndex):
        self.data = self.data.reindex(index=index.sort_values())
        x = self.data.index.to_timestamp()._mpl_repr()
    elif index.is_numeric():
        # Matplotlib supports numeric values or datetime objects as
        # xaxis values. Taking LBYL approach here, by the time
        # matplotlib raises exception when using non numeric/datetime
        # values for xaxis, several actions are already taken by plt.
        x = index._mpl_repr()
    elif is_datetype:
        self.data = self.data[notna(self.data.index)]
        self.data = self.data.sort_index()
        x = self.data.index._mpl_repr()
    else:
        self._need_to_set_index = True
        x = list(range(len(index)))
else:
    x = list(range(len(index)))

exit(x)
