# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
"""
    Convert list of dicts to numpy arrays

    if `columns` is not passed, column names are inferred from the records
    - for OrderedDict and dicts, the column names match
      the key insertion-order from the first record to the last.
    - For other kinds of dict-likes, the keys are lexically sorted.

    Parameters
    ----------
    data : iterable
        collection of records (OrderedDict, dict)
    columns: iterables or None

    Returns
    -------
    content : np.ndarray[object, ndim=2]
    columns : Index
    """
if columns is None:
    gen = (list(x.keys()) for x in data)
    sort = not any(isinstance(d, dict) for d in data)
    pre_cols = lib.fast_unique_multiple_list_gen(gen, sort=sort)
    columns = ensure_index(pre_cols)

# assure that they are of the base dict class and not of derived
# classes
data = [d if type(d) is dict else dict(d) for d in data]

content = lib.dicts_to_array(data, list(columns))
exit((content, columns))
