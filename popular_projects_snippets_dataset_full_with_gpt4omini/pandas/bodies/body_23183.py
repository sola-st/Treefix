# Extracted from ./data/repos/pandas/pandas/core/apply.py
"""
    This is the internal function to reconstruct func given if there is relabeling
    or not and also normalize the keyword to get new order of columns.

    If named aggregation is applied, `func` will be None, and kwargs contains the
    column and aggregation function information to be parsed;
    If named aggregation is not applied, `func` is either string (e.g. 'min') or
    Callable, or list of them (e.g. ['min', np.max]), or the dictionary of column name
    and str/Callable/list of them (e.g. {'A': 'min'}, or {'A': [np.min, lambda x: x]})

    If relabeling is True, will return relabeling, reconstructed func, column
    names, and the reconstructed order of columns.
    If relabeling is False, the columns and order will be None.

    Parameters
    ----------
    func: agg function (e.g. 'min' or Callable) or list of agg functions
        (e.g. ['min', np.max]) or dictionary (e.g. {'A': ['min', np.max]}).
    **kwargs: dict, kwargs used in is_multi_agg_with_relabel and
        normalize_keyword_aggregation function for relabelling

    Returns
    -------
    relabelling: bool, if there is relabelling or not
    func: normalized and mangled func
    columns: list of column names
    order: array of columns indices

    Examples
    --------
    >>> reconstruct_func(None, **{"foo": ("col", "min")})
    (True, defaultdict(<class 'list'>, {'col': ['min']}), ('foo',), array([0]))

    >>> reconstruct_func("min")
    (False, 'min', None, None)
    """
relabeling = func is None and is_multi_agg_with_relabel(**kwargs)
columns: list[str] | None = None
order: npt.NDArray[np.intp] | None = None

if not relabeling:
    if isinstance(func, list) and len(func) > len(set(func)):

        # GH 28426 will raise error if duplicated function names are used and
        # there is no reassigned name
        raise SpecificationError(
            "Function names must be unique if there is no new column names "
            "assigned"
        )
    if func is None:
        # nicer error message
        raise TypeError("Must provide 'func' or tuples of '(column, aggfunc).")

if relabeling:
    func, columns, order = normalize_keyword_aggregation(kwargs)

exit((relabeling, func, columns, order))
