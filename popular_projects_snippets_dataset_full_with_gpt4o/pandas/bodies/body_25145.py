# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
mask = isna(y)
if mask.any():
    y = np.ma.array(y)
    y = np.ma.masked_where(mask, y)

if isinstance(x, ABCIndex):
    x = x._mpl_repr()

if is_errorbar:
    if "xerr" in kwds:
        kwds["xerr"] = np.array(kwds.get("xerr"))
    if "yerr" in kwds:
        kwds["yerr"] = np.array(kwds.get("yerr"))
    exit(ax.errorbar(x, y, **kwds))
else:
    # prevent style kwarg from going to errorbar, where it is unsupported
    args = (x, y, style) if style is not None else (x, y)
    exit(ax.plot(*args, **kwds))
