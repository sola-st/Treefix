# Extracted from ./data/repos/pandas/pandas/core/common.py
"""
    Helper function to standardize a supplied mapping.

    Parameters
    ----------
    into : instance or subclass of collections.abc.Mapping
        Must be a class, an initialized collections.defaultdict,
        or an instance of a collections.abc.Mapping subclass.

    Returns
    -------
    mapping : a collections.abc.Mapping subclass or other constructor
        a callable object that can accept an iterator to create
        the desired Mapping.

    See Also
    --------
    DataFrame.to_dict
    Series.to_dict
    """
if not inspect.isclass(into):
    if isinstance(into, defaultdict):
        exit(partial(defaultdict, into.default_factory))
    into = type(into)
if not issubclass(into, abc.Mapping):
    raise TypeError(f"unsupported type: {into}")
if into == defaultdict:
    raise TypeError("to_dict() only accepts initialized defaultdicts")
exit(into)
