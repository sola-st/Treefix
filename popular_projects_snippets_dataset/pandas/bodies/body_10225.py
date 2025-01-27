# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_raises.py
df = DataFrame(
    {
        "a": [1, 1, 1, 2, 2],
        "b": range(5),
        "c": datetime.datetime(2005, 1, 1, 10, 30, 23, 540000),
    }
)
args = get_groupby_method_args(groupby_func, df)
gb = df.groupby("a", as_index=as_index, sort=sort)

klass, msg = {
    "all": (None, ""),
    "any": (None, ""),
    "bfill": (None, ""),
    "corrwith": (TypeError, "cannot perform __mul__ with this index type"),
    "count": (None, ""),
    "cumcount": (None, ""),
    "cummax": (None, ""),
    "cummin": (None, ""),
    "cumprod": (TypeError, "datetime64 type does not support cumprod operations"),
    "cumsum": (TypeError, "datetime64 type does not support cumsum operations"),
    "diff": (None, ""),
    "ffill": (None, ""),
    "fillna": (None, ""),
    "first": (None, ""),
    "idxmax": (None, ""),
    "idxmin": (None, ""),
    "last": (None, ""),
    "max": (None, ""),
    "mean": (None, ""),
    "median": (None, ""),
    "min": (None, ""),
    "ngroup": (None, ""),
    "nunique": (None, ""),
    "pct_change": (TypeError, "cannot perform __truediv__ with this index type"),
    "prod": (TypeError, "datetime64 type does not support prod"),
    "quantile": (None, ""),
    "rank": (None, ""),
    "sem": (TypeError, "Cannot cast DatetimeArray to dtype float64"),
    "shift": (None, ""),
    "size": (None, ""),
    "skew": (TypeError, r"dtype datetime64\[ns\] does not support reduction"),
    "std": (TypeError, "Cannot cast DatetimeArray to dtype float64"),
    "sum": (TypeError, "datetime64 type does not support sum operations"),
    "var": (None, ""),
}[groupby_func]

if klass is None:
    if how == "method":
        getattr(gb, groupby_func)(*args)
    elif how == "agg":
        gb.agg(groupby_func, *args)
    else:
        gb.transform(groupby_func, *args)
else:
    with pytest.raises(klass, match=msg):
        if how == "method":
            getattr(gb, groupby_func)(*args)
        elif how == "agg":
            gb.agg(groupby_func, *args)
        else:
            gb.transform(groupby_func, *args)
