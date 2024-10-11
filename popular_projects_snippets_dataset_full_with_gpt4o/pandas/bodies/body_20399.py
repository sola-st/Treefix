# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        Convert list of tuples to MultiIndex.

        Parameters
        ----------
        tuples : list / sequence of tuple-likes
            Each tuple is the index of one row/column.
        sortorder : int or None
            Level of sortedness (must be lexicographically sorted by that
            level).
        names : list / sequence of str, optional
            Names for the levels in the index.

        Returns
        -------
        MultiIndex

        See Also
        --------
        MultiIndex.from_arrays : Convert list of arrays to MultiIndex.
        MultiIndex.from_product : Make a MultiIndex from cartesian product
                                  of iterables.
        MultiIndex.from_frame : Make a MultiIndex from a DataFrame.

        Examples
        --------
        >>> tuples = [(1, 'red'), (1, 'blue'),
        ...           (2, 'red'), (2, 'blue')]
        >>> pd.MultiIndex.from_tuples(tuples, names=('number', 'color'))
        MultiIndex([(1,  'red'),
                    (1, 'blue'),
                    (2,  'red'),
                    (2, 'blue')],
                   names=['number', 'color'])
        """
if not is_list_like(tuples):
    raise TypeError("Input must be a list / sequence of tuple-likes.")
if is_iterator(tuples):
    tuples = list(tuples)
tuples = cast(Collection[Tuple[Hashable, ...]], tuples)

# handling the empty tuple cases
if len(tuples) and all(isinstance(e, tuple) and not e for e in tuples):
    codes = [np.zeros(len(tuples))]
    levels = [Index(com.asarray_tuplesafe(tuples, dtype=np.dtype("object")))]
    exit(cls(
        levels=levels,
        codes=codes,
        sortorder=sortorder,
        names=names,
        verify_integrity=False,
    ))

arrays: list[Sequence[Hashable]]
if len(tuples) == 0:
    if names is None:
        raise TypeError("Cannot infer number of levels from empty list")
    # error: Argument 1 to "len" has incompatible type "Hashable";
    # expected "Sized"
    arrays = [[]] * len(names)  # type: ignore[arg-type]
elif isinstance(tuples, (np.ndarray, Index)):
    if isinstance(tuples, Index):
        tuples = np.asarray(tuples._values)

    arrays = list(lib.tuples_to_object_array(tuples).T)
elif isinstance(tuples, list):
    arrays = list(lib.to_object_array_tuples(tuples).T)
else:
    arrs = zip(*tuples)
    arrays = cast(List[Sequence[Hashable]], arrs)

exit(cls.from_arrays(arrays, sortorder=sortorder, names=names))
