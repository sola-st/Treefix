# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""
    Sort ``values`` and reorder corresponding ``codes``.

    ``values`` should be unique if ``codes`` is not None.
    Safe for use with mixed types (int, str), orders ints before strs.

    Parameters
    ----------
    values : list-like
        Sequence; must be unique if ``codes`` is not None.
    codes : list_like, optional
        Indices to ``values``. All out of bound indices are treated as
        "not found" and will be masked with ``-1``.
    use_na_sentinel : bool, default True
        If True, the sentinel -1 will be used for NaN values. If False,
        NaN values will be encoded as non-negative integers and will not drop the
        NaN from the uniques of the values.
    assume_unique : bool, default False
        When True, ``values`` are assumed to be unique, which can speed up
        the calculation. Ignored when ``codes`` is None.
    verify : bool, default True
        Check if codes are out of bound for the values and put out of bound
        codes equal to ``-1``. If ``verify=False``, it is assumed there
        are no out of bound codes. Ignored when ``codes`` is None.

    Returns
    -------
    ordered : AnyArrayLike
        Sorted ``values``
    new_codes : ndarray
        Reordered ``codes``; returned when ``codes`` is not None.

    Raises
    ------
    TypeError
        * If ``values`` is not list-like or if ``codes`` is neither None
        nor list-like
        * If ``values`` cannot be sorted
    ValueError
        * If ``codes`` is not None and ``values`` contain duplicates.
    """
if not is_list_like(values):
    raise TypeError(
        "Only list-like objects are allowed to be passed to safe_sort as values"
    )

if not is_array_like(values):
    # don't convert to string types
    dtype, _ = infer_dtype_from_array(values)
    # error: Argument "dtype" to "asarray" has incompatible type "Union[dtype[Any],
    # ExtensionDtype]"; expected "Union[dtype[Any], None, type, _SupportsDType, str,
    # Union[Tuple[Any, int], Tuple[Any, Union[int, Sequence[int]]], List[Any],
    # _DTypeDict, Tuple[Any, Any]]]"
    values = np.asarray(values, dtype=dtype)  # type: ignore[arg-type]

sorter = None
ordered: AnyArrayLike

if (
    not is_extension_array_dtype(values)
    and lib.infer_dtype(values, skipna=False) == "mixed-integer"
):
    ordered = _sort_mixed(values)
else:
    try:
        sorter = values.argsort()
        ordered = values.take(sorter)
    except TypeError:
        # Previous sorters failed or were not applicable, try `_sort_mixed`
        # which would work, but which fails for special case of 1d arrays
        # with tuples.
        if values.size and isinstance(values[0], tuple):
            ordered = _sort_tuples(values)
        else:
            ordered = _sort_mixed(values)

    # codes:

if codes is None:
    exit(ordered)

if not is_list_like(codes):
    raise TypeError(
        "Only list-like objects or None are allowed to "
        "be passed to safe_sort as codes"
    )
codes = ensure_platform_int(np.asarray(codes))

if not assume_unique and not len(unique(values)) == len(values):
    raise ValueError("values should be unique if codes is not None")

if sorter is None:
    # mixed types
    hash_klass, values = _get_hashtable_algo(values)
    t = hash_klass(len(values))
    t.map_locations(values)
    sorter = ensure_platform_int(t.lookup(ordered))

if use_na_sentinel:
    # take_nd is faster, but only works for na_sentinels of -1
    order2 = sorter.argsort()
    new_codes = take_nd(order2, codes, fill_value=-1)
    if verify:
        mask = (codes < -len(values)) | (codes >= len(values))
    else:
        mask = None
else:
    reverse_indexer = np.empty(len(sorter), dtype=np.int_)
    reverse_indexer.put(sorter, np.arange(len(sorter)))
    # Out of bound indices will be masked with `-1` next, so we
    # may deal with them here without performance loss using `mode='wrap'`
    new_codes = reverse_indexer.take(codes, mode="wrap")

    if use_na_sentinel:
        mask = codes == -1
        if verify:
            mask = mask | (codes < -len(values)) | (codes >= len(values))

if use_na_sentinel and mask is not None:
    np.putmask(new_codes, mask, -1)

exit((ordered, ensure_platform_int(new_codes)))
