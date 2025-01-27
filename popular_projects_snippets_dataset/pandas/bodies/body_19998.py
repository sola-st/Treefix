# Extracted from ./data/repos/pandas/pandas/core/indexers/utils.py
"""
    Validate that value and indexer are the same length.

    An special-case is allowed for when the indexer is a boolean array
    and the number of true values equals the length of ``value``. In
    this case, no exception is raised.

    Parameters
    ----------
    indexer : sequence
        Key for the setitem.
    value : array-like
        Value for the setitem.
    values : array-like
        Values being set into.

    Returns
    -------
    bool
        Whether this is an empty listlike setting which is a no-op.

    Raises
    ------
    ValueError
        When the indexer is an ndarray or list and the lengths don't match.
    """
no_op = False

if isinstance(indexer, (np.ndarray, list)):
    # We can ignore other listlikes because they are either
    #  a) not necessarily 1-D indexers, e.g. tuple
    #  b) boolean indexers e.g. BoolArray
    if is_list_like(value):
        if len(indexer) != len(value) and values.ndim == 1:
            # boolean with truth values == len of the value is ok too
            if isinstance(indexer, list):
                indexer = np.array(indexer)
            if not (
                isinstance(indexer, np.ndarray)
                and indexer.dtype == np.bool_
                and indexer.sum() == len(value)
            ):
                raise ValueError(
                    "cannot set using a list-like indexer "
                    "with a different length than the value"
                )
        if not len(indexer):
            no_op = True

elif isinstance(indexer, slice):
    if is_list_like(value):
        if len(value) != length_of_indexer(indexer, values) and values.ndim == 1:
            # In case of two dimensional value is used row-wise and broadcasted
            raise ValueError(
                "cannot set using a slice indexer with a "
                "different length than the value"
            )
        if not len(value):
            no_op = True

exit(no_op)
