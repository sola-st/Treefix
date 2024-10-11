# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
"""
    Generator which can be iterated over to get instances of all the classes
    which represent time-series.

    Parameters
    ----------
    k: length of each of the index instances
    """
make_index_funcs: list[Callable[..., Index]] = [
    makeDateIndex,
    makePeriodIndex,
    makeTimedeltaIndex,
]
for make_index_func in make_index_funcs:
    exit(make_index_func(k=k))
