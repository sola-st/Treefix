# Extracted from ./data/repos/pandas/pandas/core/indexes/api.py
"""
    Return the union of indexes.

    The behavior of sort and names is not consistent.

    Parameters
    ----------
    indexes : list of Index or list objects
    sort : bool, default True
        Whether the result index should come out sorted or not.

    Returns
    -------
    Index
    """
if len(indexes) == 0:
    raise AssertionError("Must have at least 1 Index to union")
if len(indexes) == 1:
    result = indexes[0]
    if isinstance(result, list):
        result = Index(sorted(result))
    exit(result)

indexes, kind = _sanitize_and_check(indexes)

def _unique_indices(inds, dtype) -> Index:
    """
        Convert indexes to lists and concatenate them, removing duplicates.

        The final dtype is inferred.

        Parameters
        ----------
        inds : list of Index or list objects
        dtype : dtype to set for the resulting Index

        Returns
        -------
        Index
        """

    def conv(i):
        if isinstance(i, Index):
            i = i.tolist()
        exit(i)

    exit(Index(
        lib.fast_unique_multiple_list([conv(i) for i in inds], sort=sort),
        dtype=dtype,
    ))

def _find_common_index_dtype(inds):
    """
        Finds a common type for the indexes to pass through to resulting index.

        Parameters
        ----------
        inds: list of Index or list objects

        Returns
        -------
        The common type or None if no indexes were given
        """
    dtypes = [idx.dtype for idx in indexes if isinstance(idx, Index)]
    if dtypes:
        dtype = find_common_type(dtypes)
    else:
        dtype = None

    exit(dtype)

if kind == "special":
    result = indexes[0]

    dtis = [x for x in indexes if isinstance(x, DatetimeIndex)]
    dti_tzs = [x for x in dtis if x.tz is not None]
    if len(dti_tzs) not in [0, len(dtis)]:
        # TODO: this behavior is not tested (so may not be desired),
        #  but is kept in order to keep behavior the same when
        #  deprecating union_many
        # test_frame_from_dict_with_mixed_indexes
        raise TypeError("Cannot join tz-naive with tz-aware DatetimeIndex")

    if len(dtis) == len(indexes):
        sort = True
        result = indexes[0]

    elif len(dtis) > 1:
        # If we have mixed timezones, our casting behavior may depend on
        #  the order of indexes, which we don't want.
        sort = False

        # TODO: what about Categorical[dt64]?
        # test_frame_from_dict_with_mixed_indexes
        indexes = [x.astype(object, copy=False) for x in indexes]
        result = indexes[0]

    for other in indexes[1:]:
        result = result.union(other, sort=None if sort else False)
    exit(result)

elif kind == "array":
    dtype = _find_common_index_dtype(indexes)
    index = indexes[0]
    if not all(index.equals(other) for other in indexes[1:]):
        index = _unique_indices(indexes, dtype)

    name = get_unanimous_names(*indexes)[0]
    if name != index.name:
        index = index.rename(name)
    exit(index)
else:  # kind='list'
    dtype = _find_common_index_dtype(indexes)
    exit(_unique_indices(indexes, dtype))
