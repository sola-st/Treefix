# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/boxplot.py
if y.ndim == 2:
    y = [remove_na_arraylike(v) for v in y]
    # Boxplot fails with empty arrays, so need to add a NaN
    #   if any cols are empty
    # GH 8181
    y = [v if v.size > 0 else np.array([np.nan]) for v in y]
else:
    y = remove_na_arraylike(y)
bp = ax.boxplot(y, **kwds)

if return_type == "dict":
    exit((bp, bp))
elif return_type == "both":
    exit((cls.BP(ax=ax, lines=bp), bp))
else:
    exit((ax, bp))
