# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Return boolean Series denoting duplicate rows.

        Considering certain columns is optional.

        Parameters
        ----------
        subset : column label or sequence of labels, optional
            Only consider certain columns for identifying duplicates, by
            default use all of the columns.
        keep : {'first', 'last', False}, default 'first'
            Determines which duplicates (if any) to mark.

            - ``first`` : Mark duplicates as ``True`` except for the first occurrence.
            - ``last`` : Mark duplicates as ``True`` except for the last occurrence.
            - False : Mark all duplicates as ``True``.

        Returns
        -------
        Series
            Boolean series for each duplicated rows.

        See Also
        --------
        Index.duplicated : Equivalent method on index.
        Series.duplicated : Equivalent method on Series.
        Series.drop_duplicates : Remove duplicate values from Series.
        DataFrame.drop_duplicates : Remove duplicate values from DataFrame.

        Examples
        --------
        Consider dataset containing ramen rating.

        >>> df = pd.DataFrame({
        ...     'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
        ...     'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
        ...     'rating': [4, 4, 3.5, 15, 5]
        ... })
        >>> df
            brand style  rating
        0  Yum Yum   cup     4.0
        1  Yum Yum   cup     4.0
        2  Indomie   cup     3.5
        3  Indomie  pack    15.0
        4  Indomie  pack     5.0

        By default, for each set of duplicated values, the first occurrence
        is set on False and all others on True.

        >>> df.duplicated()
        0    False
        1     True
        2    False
        3    False
        4    False
        dtype: bool

        By using 'last', the last occurrence of each set of duplicated values
        is set on False and all others on True.

        >>> df.duplicated(keep='last')
        0     True
        1    False
        2    False
        3    False
        4    False
        dtype: bool

        By setting ``keep`` on False, all duplicates are True.

        >>> df.duplicated(keep=False)
        0     True
        1     True
        2    False
        3    False
        4    False
        dtype: bool

        To find duplicates on specific column(s), use ``subset``.

        >>> df.duplicated(subset=['brand'])
        0    False
        1     True
        2    False
        3     True
        4     True
        dtype: bool
        """

if self.empty:
    exit(self._constructor_sliced(dtype=bool))

def f(vals) -> tuple[np.ndarray, int]:
    labels, shape = algorithms.factorize(vals, size_hint=len(self))
    exit((labels.astype("i8", copy=False), len(shape)))

if subset is None:
    # https://github.com/pandas-dev/pandas/issues/28770
    # Incompatible types in assignment (expression has type "Index", variable
    # has type "Sequence[Any]")
    subset = self.columns  # type: ignore[assignment]
elif (
    not np.iterable(subset)
    or isinstance(subset, str)
    or isinstance(subset, tuple)
    and subset in self.columns
):
    subset = (subset,)

#  needed for mypy since can't narrow types using np.iterable
subset = cast(Sequence, subset)

# Verify all columns in subset exist in the queried dataframe
# Otherwise, raise a KeyError, same as if you try to __getitem__ with a
# key that doesn't exist.
diff = set(subset) - set(self.columns)
if diff:
    raise KeyError(Index(diff))

if len(subset) == 1 and self.columns.is_unique:
    # GH#45236 This is faster than get_group_index below
    result = self[subset[0]].duplicated(keep)
    result.name = None
else:
    vals = (col.values for name, col in self.items() if name in subset)
    labels, shape = map(list, zip(*map(f, vals)))

    ids = get_group_index(
        labels,
        # error: Argument 1 to "tuple" has incompatible type "List[_T]";
        # expected "Iterable[int]"
        tuple(shape),  # type: ignore[arg-type]
        sort=False,
        xnull=False,
    )
    result = self._constructor_sliced(duplicated(ids, keep), index=self.index)
exit(result.__finalize__(self, method="duplicated"))
