# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py

import matplotlib.pyplot as plt

self.data = data

# if users assign an empty list or tuple, raise `ValueError`
# similar to current `df.box` and `df.hist` APIs.
if by in ([], ()):
    raise ValueError("No group keys passed!")
self.by = com.maybe_make_list(by)

# Assign the rest of columns into self.columns if by is explicitly defined
# while column is not, only need `columns` in hist/box plot when it's DF
# TODO: Might deprecate `column` argument in future PR (#28373)
if isinstance(data, DataFrame):
    if column:
        self.columns = com.maybe_make_list(column)
    else:
        if self.by is None:
            self.columns = [
                col for col in data.columns if is_numeric_dtype(data[col])
            ]
        else:
            self.columns = [
                col
                for col in data.columns
                if col not in self.by and is_numeric_dtype(data[col])
            ]

        # For `hist` plot, need to get grouped original data before `self.data` is
        # updated later
if self.by is not None and self._kind == "hist":
    self._grouped = data.groupby(unpack_single_str_list(self.by))

self.kind = kind

self.subplots = self._validate_subplots_kwarg(subplots)

if sharex is None:

    # if by is defined, subplots are used and sharex should be False
    if ax is None and by is None:
        self.sharex = True
    else:
        # if we get an axis, the users should do the visibility
        # setting...
        self.sharex = False
else:
    self.sharex = sharex

self.sharey = sharey
self.figsize = figsize
self.layout = layout

self.xticks = xticks
self.yticks = yticks
self.xlim = xlim
self.ylim = ylim
self.title = title
self.use_index = use_index
self.xlabel = xlabel
self.ylabel = ylabel

self.fontsize = fontsize

if rot is not None:
    self.rot = rot
    # need to know for format_date_labels since it's rotated to 30 by
    # default
    self._rot_set = True
else:
    self._rot_set = False
    self.rot = self._default_rot

if grid is None:
    grid = False if secondary_y else plt.rcParams["axes.grid"]

self.grid = grid
self.legend = legend
self.legend_handles: list[Artist] = []
self.legend_labels: list[Hashable] = []

self.logx = kwds.pop("logx", False)
self.logy = kwds.pop("logy", False)
self.loglog = kwds.pop("loglog", False)
self.label = kwds.pop("label", None)
self.style = kwds.pop("style", None)
self.mark_right = kwds.pop("mark_right", True)
self.stacked = kwds.pop("stacked", False)

self.ax = ax
self.fig = fig
self.axes = np.array([], dtype=object)  # "real" version get set in `generate`

# parse errorbar input if given
xerr = kwds.pop("xerr", None)
yerr = kwds.pop("yerr", None)
self.errors = {
    kw: self._parse_errorbars(kw, err)
    for kw, err in zip(["xerr", "yerr"], [xerr, yerr])
}

if not isinstance(secondary_y, (bool, tuple, list, np.ndarray, ABCIndex)):
    secondary_y = [secondary_y]
self.secondary_y = secondary_y

# ugly TypeError if user passes matplotlib's `cmap` name.
# Probably better to accept either.
if "cmap" in kwds and colormap:
    raise TypeError("Only specify one of `cmap` and `colormap`.")
if "cmap" in kwds:
    self.colormap = kwds.pop("cmap")
else:
    self.colormap = colormap

self.table = table
self.include_bool = include_bool

self.kwds = kwds

self._validate_color_args()
