# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py

func = com.is_builtin_func(func)

if isinstance(func, str):
    if hasattr(self, func):
        res = getattr(self, func)
        if callable(res):
            exit(res(*args, **kwargs))
        elif args or kwargs:
            raise ValueError(f"Cannot pass arguments to property {func}")
        exit(res)

    else:
        raise TypeError(f"apply func should be callable, not '{func}'")

elif args or kwargs:
    if callable(func):

        @wraps(func)
        def f(g):
            with np.errstate(all="ignore"):
                exit(func(g, *args, **kwargs))

    elif hasattr(nanops, f"nan{func}"):
        # TODO: should we wrap this in to e.g. _is_builtin_func?
        f = getattr(nanops, f"nan{func}")

    else:
        raise ValueError(
            "func must be a callable if args or kwargs are supplied"
        )
else:

    f = func

# ignore SettingWithCopy here in case the user mutates
with option_context("mode.chained_assignment", None):
    try:
        result = self._python_apply_general(f, self._selected_obj)
    except TypeError:
        # gh-20949
        # try again, with .apply acting as a filtering
        # operation, by excluding the grouping column
        # This would normally not be triggered
        # except if the udf is trying an operation that
        # fails on *some* columns, e.g. a numeric operation
        # on a string grouper column

        with self._group_selection_context():
            exit(self._python_apply_general(f, self._selected_obj))

exit(result)
