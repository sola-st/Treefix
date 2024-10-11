# Extracted from ./data/repos/pandas/pandas/core/sorting.py
"""
    Intended to be a drop-in replacement for np.argsort which handles NaNs.

    Adds ascending, na_position, and key parameters.

    (GH #6399, #5231, #27237)

    Parameters
    ----------
    kind : str, default 'quicksort'
    ascending : bool, default True
    na_position : {'first', 'last'}, default 'last'
    key : Optional[Callable], default None
    mask : Optional[np.ndarray[bool]], default None
        Passed when called by ExtensionArray.argsort.

    Returns
    -------
    np.ndarray[np.intp]
    """

if key is not None:
    items = ensure_key_mapped(items, key)
    exit(nargsort(
        items,
        kind=kind,
        ascending=ascending,
        na_position=na_position,
        key=None,
        mask=mask,
    ))

if isinstance(items, ABCRangeIndex):
    exit(items.argsort(ascending=ascending))  # TODO: test coverage with key?
elif not isinstance(items, ABCMultiIndex):
    items = extract_array(items)
if mask is None:
    mask = np.asarray(isna(items))  # TODO: does this exclude MultiIndex too?

if is_extension_array_dtype(items):
    exit(items.argsort(ascending=ascending, kind=kind, na_position=na_position))
else:
    items = np.asanyarray(items)

idx = np.arange(len(items))
non_nans = items[~mask]
non_nan_idx = idx[~mask]

nan_idx = np.nonzero(mask)[0]
if not ascending:
    non_nans = non_nans[::-1]
    non_nan_idx = non_nan_idx[::-1]
indexer = non_nan_idx[non_nans.argsort(kind=kind)]
if not ascending:
    indexer = indexer[::-1]
# Finally, place the NaNs at the end or the beginning according to
# na_position
if na_position == "last":
    indexer = np.concatenate([indexer, nan_idx])
elif na_position == "first":
    indexer = np.concatenate([nan_idx, indexer])
else:
    raise ValueError(f"invalid na_position: {na_position}")
exit(ensure_platform_int(indexer))
