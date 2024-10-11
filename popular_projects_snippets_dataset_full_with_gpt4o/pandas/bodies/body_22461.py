# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Transpose index and columns.

        Reflect the DataFrame over its main diagonal by writing rows as columns
        and vice-versa. The property :attr:`.T` is an accessor to the method
        :meth:`transpose`.

        Parameters
        ----------
        *args : tuple, optional
            Accepted for compatibility with NumPy.
        copy : bool, default False
            Whether to copy the data after transposing, even for DataFrames
            with a single dtype.

            Note that a copy is always required for mixed dtype DataFrames,
            or for DataFrames with any extension types.

        Returns
        -------
        DataFrame
            The transposed DataFrame.

        See Also
        --------
        numpy.transpose : Permute the dimensions of a given array.

        Notes
        -----
        Transposing a DataFrame with mixed dtypes will result in a homogeneous
        DataFrame with the `object` dtype. In such a case, a copy of the data
        is always made.

        Examples
        --------
        **Square DataFrame with homogeneous dtype**

        >>> d1 = {'col1': [1, 2], 'col2': [3, 4]}
        >>> df1 = pd.DataFrame(data=d1)
        >>> df1
           col1  col2
        0     1     3
        1     2     4

        >>> df1_transposed = df1.T  # or df1.transpose()
        >>> df1_transposed
              0  1
        col1  1  2
        col2  3  4

        When the dtype is homogeneous in the original DataFrame, we get a
        transposed DataFrame with the same dtype:

        >>> df1.dtypes
        col1    int64
        col2    int64
        dtype: object
        >>> df1_transposed.dtypes
        0    int64
        1    int64
        dtype: object

        **Non-square DataFrame with mixed dtypes**

        >>> d2 = {'name': ['Alice', 'Bob'],
        ...       'score': [9.5, 8],
        ...       'employed': [False, True],
        ...       'kids': [0, 0]}
        >>> df2 = pd.DataFrame(data=d2)
        >>> df2
            name  score  employed  kids
        0  Alice    9.5     False     0
        1    Bob    8.0      True     0

        >>> df2_transposed = df2.T  # or df2.transpose()
        >>> df2_transposed
                      0     1
        name      Alice   Bob
        score       9.5   8.0
        employed  False  True
        kids          0     0

        When the DataFrame has mixed dtypes, we get a transposed DataFrame with
        the `object` dtype:

        >>> df2.dtypes
        name         object
        score       float64
        employed       bool
        kids          int64
        dtype: object
        >>> df2_transposed.dtypes
        0    object
        1    object
        dtype: object
        """
nv.validate_transpose(args, {})
# construct the args

dtypes = list(self.dtypes)

if self._can_fast_transpose:
    # Note: tests pass without this, but this improves perf quite a bit.
    new_vals = self._values.T
    if copy:
        new_vals = new_vals.copy()

    result = self._constructor(new_vals, index=self.columns, columns=self.index)

elif (
    self._is_homogeneous_type and dtypes and is_extension_array_dtype(dtypes[0])
):
    # We have EAs with the same dtype. We can preserve that dtype in transpose.
    dtype = dtypes[0]
    arr_type = dtype.construct_array_type()
    values = self.values

    new_values = [arr_type._from_sequence(row, dtype=dtype) for row in values]
    result = type(self)._from_arrays(
        new_values, index=self.columns, columns=self.index
    )

else:
    new_arr = self.values.T
    if copy:
        new_arr = new_arr.copy()
    result = self._constructor(new_arr, index=self.columns, columns=self.index)

exit(result.__finalize__(self, method="transpose"))
