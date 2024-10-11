# Extracted from ./data/repos/pandas/pandas/plotting/_core.py
"""
        This function makes calls to this accessor `__call__` method compatible
        with the previous `SeriesPlotMethods.__call__` and
        `DataFramePlotMethods.__call__`. Those had slightly different
        signatures, since `DataFramePlotMethods` accepted `x` and `y`
        parameters.
        """
if isinstance(data, ABCSeries):
    arg_def = [
        ("kind", "line"),
        ("ax", None),
        ("figsize", None),
        ("use_index", True),
        ("title", None),
        ("grid", None),
        ("legend", False),
        ("style", None),
        ("logx", False),
        ("logy", False),
        ("loglog", False),
        ("xticks", None),
        ("yticks", None),
        ("xlim", None),
        ("ylim", None),
        ("rot", None),
        ("fontsize", None),
        ("colormap", None),
        ("table", False),
        ("yerr", None),
        ("xerr", None),
        ("label", None),
        ("secondary_y", False),
        ("xlabel", None),
        ("ylabel", None),
    ]
elif isinstance(data, ABCDataFrame):
    arg_def = [
        ("x", None),
        ("y", None),
        ("kind", "line"),
        ("ax", None),
        ("subplots", False),
        ("sharex", None),
        ("sharey", False),
        ("layout", None),
        ("figsize", None),
        ("use_index", True),
        ("title", None),
        ("grid", None),
        ("legend", True),
        ("style", None),
        ("logx", False),
        ("logy", False),
        ("loglog", False),
        ("xticks", None),
        ("yticks", None),
        ("xlim", None),
        ("ylim", None),
        ("rot", None),
        ("fontsize", None),
        ("colormap", None),
        ("table", False),
        ("yerr", None),
        ("xerr", None),
        ("secondary_y", False),
        ("xlabel", None),
        ("ylabel", None),
    ]
else:
    raise TypeError(
        f"Called plot accessor for type {type(data).__name__}, "
        "expected Series or DataFrame"
    )

if args and isinstance(data, ABCSeries):
    positional_args = str(args)[1:-1]
    keyword_args = ", ".join(
        [f"{name}={repr(value)}" for (name, _), value in zip(arg_def, args)]
    )
    msg = (
        "`Series.plot()` should not be called with positional "
        "arguments, only keyword arguments. The order of "
        "positional arguments will change in the future. "
        f"Use `Series.plot({keyword_args})` instead of "
        f"`Series.plot({positional_args})`."
    )
    raise TypeError(msg)

pos_args = {name: value for (name, _), value in zip(arg_def, args)}
if backend_name == "pandas.plotting._matplotlib":
    kwargs = dict(arg_def, **pos_args, **kwargs)
else:
    kwargs = dict(pos_args, **kwargs)

x = kwargs.pop("x", None)
y = kwargs.pop("y", None)
kind = kwargs.pop("kind", "line")
exit((x, y, kind, kwargs))
