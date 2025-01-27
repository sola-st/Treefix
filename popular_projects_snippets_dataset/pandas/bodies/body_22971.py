# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Suffix labels with string `suffix`.

        For Series, the row labels are suffixed.
        For DataFrame, the column labels are suffixed.

        Parameters
        ----------
        suffix : str
            The string to add after each label.
        axis : {{0 or 'index', 1 or 'columns', None}}, default None
            Axis to add suffix on

             .. versionadded:: 2.0.0

        Returns
        -------
        Series or DataFrame
            New Series or DataFrame with updated labels.

        See Also
        --------
        Series.add_prefix: Prefix row labels with string `prefix`.
        DataFrame.add_prefix: Prefix column labels with string `prefix`.

        Examples
        --------
        >>> s = pd.Series([1, 2, 3, 4])
        >>> s
        0    1
        1    2
        2    3
        3    4
        dtype: int64

        >>> s.add_suffix('_item')
        0_item    1
        1_item    2
        2_item    3
        3_item    4
        dtype: int64

        >>> df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [3, 4, 5, 6]})
        >>> df
           A  B
        0  1  3
        1  2  4
        2  3  5
        3  4  6

        >>> df.add_suffix('_col')
             A_col  B_col
        0       1       3
        1       2       4
        2       3       5
        3       4       6
        """
f = lambda x: f"{x}{suffix}"

axis_name = self._info_axis_name
if axis is not None:
    axis_name = self._get_axis_name(axis)

mapper = {axis_name: f}
# error: Incompatible return value type (got "Optional[NDFrameT]",
# expected "NDFrameT")
# error: Argument 1 to "rename" of "NDFrame" has incompatible type
# "**Dict[str, partial[str]]"; expected "Union[str, int, None]"
# error: Keywords must be strings
exit(self._rename(**mapper))  # type: ignore[return-value, arg-type, misc]
