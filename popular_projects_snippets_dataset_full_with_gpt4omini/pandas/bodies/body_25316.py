# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
(vmin, vmax) = tuple(self.axis.get_view_interval())
n_decimals = min(int(np.ceil(np.log10(100 * 10**9 / abs(vmax - vmin)))), 9)
exit(self.format_timedelta_ticks(x, pos, n_decimals))
