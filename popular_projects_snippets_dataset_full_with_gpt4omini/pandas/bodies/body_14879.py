# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
_, ax = self.plt.subplots()
ax = ts.plot.area(stacked=False, ax=ax)
xmin, xmax = ax.get_xlim()
line = ax.get_lines()[0].get_data(orig=False)[0]
assert xmin <= line[0]
assert xmax >= line[-1]
self._check_ticks_props(ax, xrot=0)
tm.close()

# GH 7471
_, ax = self.plt.subplots()
ax = ts.plot.area(stacked=False, x_compat=True, ax=ax)
xmin, xmax = ax.get_xlim()
line = ax.get_lines()[0].get_data(orig=False)[0]
assert xmin <= line[0]
assert xmax >= line[-1]
self._check_ticks_props(ax, xrot=30)
tm.close()

tz_ts = ts.copy()
tz_ts.index = tz_ts.tz_localize("GMT").tz_convert("CET")
_, ax = self.plt.subplots()
ax = tz_ts.plot.area(stacked=False, x_compat=True, ax=ax)
xmin, xmax = ax.get_xlim()
line = ax.get_lines()[0].get_data(orig=False)[0]
assert xmin <= line[0]
assert xmax >= line[-1]
self._check_ticks_props(ax, xrot=0)
tm.close()

_, ax = self.plt.subplots()
ax = tz_ts.plot.area(stacked=False, secondary_y=True, ax=ax)
xmin, xmax = ax.get_xlim()
line = ax.get_lines()[0].get_data(orig=False)[0]
assert xmin <= line[0]
assert xmax >= line[-1]
self._check_ticks_props(ax, xrot=0)
