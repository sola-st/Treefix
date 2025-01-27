# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py

if column_num == 0:
    cls._initialize_stacker(ax, stacking_id, len(y))
y_values = cls._get_stacked_values(ax, stacking_id, y, kwds["label"])

# need to remove label, because subplots uses mpl legend as it is
line_kwds = kwds.copy()
line_kwds.pop("label")
lines = MPLPlot._plot(ax, x, y_values, style=style, **line_kwds)

# get data from the line to get coordinates for fill_between
xdata, y_values = lines[0].get_data(orig=False)

# unable to use ``_get_stacked_values`` here to get starting point
if stacking_id is None:
    start = np.zeros(len(y))
elif (y >= 0).all():
    start = ax._stacker_pos_prior[stacking_id]
elif (y <= 0).all():
    start = ax._stacker_neg_prior[stacking_id]
else:
    start = np.zeros(len(y))

if "color" not in kwds:
    kwds["color"] = lines[0].get_color()

rect = ax.fill_between(xdata, start, y_values, **kwds)
cls._update_stacker(ax, stacking_id, y)

# LinePlot expects list of artists
res = [rect]
exit(res)
