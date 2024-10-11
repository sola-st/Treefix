# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_raises.py
df = DataFrame(
    {
        "a": [1, 1, 1, 2, 2],
        "b": range(5),
        "c": list("xyzwt"),
    }
)
args = get_groupby_method_args(groupby_func, df)
gb = df.groupby("a", as_index=as_index, sort=sort)

klass, msg = {
    "all": (None, ""),
    "any": (None, ""),
    "bfill": (None, ""),
    "corrwith": (TypeError, "Could not convert"),
    "count": (None, ""),
    "cumcount": (None, ""),
    "cummax": (NotImplementedError, "function is not implemented for this dtype"),
    "cummin": (NotImplementedError, "function is not implemented for this dtype"),
    "cumprod": (NotImplementedError, "function is not implemented for this dtype"),
    "cumsum": (NotImplementedError, "function is not implemented for this dtype"),
    "diff": (TypeError, "unsupported operand type"),
    "ffill": (None, ""),
    "fillna": (None, ""),
    "first": (None, ""),
    "idxmax": (TypeError, "'argmax' not allowed for this dtype"),
    "idxmin": (TypeError, "'argmin' not allowed for this dtype"),
    "last": (None, ""),
    "max": (None, ""),
    "mean": (TypeError, "Could not convert xyz to numeric"),
    "median": (TypeError, "could not convert string to float"),
    "min": (None, ""),
    "ngroup": (None, ""),
    "nunique": (None, ""),
    "pct_change": (TypeError, "unsupported operand type"),
    "prod": (TypeError, "can't multiply sequence by non-int of type 'str'"),
    "quantile": (TypeError, "cannot be performed against 'object' dtypes!"),
    "rank": (None, ""),
    "sem": (ValueError, "could not convert string to float"),
    "shift": (None, ""),
    "size": (None, ""),
    "skew": (TypeError, "could not convert string to float"),
    "std": (ValueError, "could not convert string to float"),
    "sum": (None, ""),
    "var": (TypeError, "could not convert string to float"),
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
