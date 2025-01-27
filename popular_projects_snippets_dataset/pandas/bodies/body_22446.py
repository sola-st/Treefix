# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Convert DataFrame to a NumPy record array.

        Index will be included as the first field of the record array if
        requested.

        Parameters
        ----------
        index : bool, default True
            Include index in resulting record array, stored in 'index'
            field or using the index label, if set.
        column_dtypes : str, type, dict, default None
            If a string or type, the data type to store all columns. If
            a dictionary, a mapping of column names and indices (zero-indexed)
            to specific data types.
        index_dtypes : str, type, dict, default None
            If a string or type, the data type to store all index levels. If
            a dictionary, a mapping of index level names and indices
            (zero-indexed) to specific data types.

            This mapping is applied only if `index=True`.

        Returns
        -------
        numpy.recarray
            NumPy ndarray with the DataFrame labels as fields and each row
            of the DataFrame as entries.

        See Also
        --------
        DataFrame.from_records: Convert structured or record ndarray
            to DataFrame.
        numpy.recarray: An ndarray that allows field access using
            attributes, analogous to typed columns in a
            spreadsheet.

        Examples
        --------
        >>> df = pd.DataFrame({'A': [1, 2], 'B': [0.5, 0.75]},
        ...                   index=['a', 'b'])
        >>> df
           A     B
        a  1  0.50
        b  2  0.75
        >>> df.to_records()
        rec.array([('a', 1, 0.5 ), ('b', 2, 0.75)],
                  dtype=[('index', 'O'), ('A', '<i8'), ('B', '<f8')])

        If the DataFrame index has no label then the recarray field name
        is set to 'index'. If the index has a label then this is used as the
        field name:

        >>> df.index = df.index.rename("I")
        >>> df.to_records()
        rec.array([('a', 1, 0.5 ), ('b', 2, 0.75)],
                  dtype=[('I', 'O'), ('A', '<i8'), ('B', '<f8')])

        The index can be excluded from the record array:

        >>> df.to_records(index=False)
        rec.array([(1, 0.5 ), (2, 0.75)],
                  dtype=[('A', '<i8'), ('B', '<f8')])

        Data types can be specified for the columns:

        >>> df.to_records(column_dtypes={"A": "int32"})
        rec.array([('a', 1, 0.5 ), ('b', 2, 0.75)],
                  dtype=[('I', 'O'), ('A', '<i4'), ('B', '<f8')])

        As well as for the index:

        >>> df.to_records(index_dtypes="<S2")
        rec.array([(b'a', 1, 0.5 ), (b'b', 2, 0.75)],
                  dtype=[('I', 'S2'), ('A', '<i8'), ('B', '<f8')])

        >>> index_dtypes = f"<S{df.index.str.len().max()}"
        >>> df.to_records(index_dtypes=index_dtypes)
        rec.array([(b'a', 1, 0.5 ), (b'b', 2, 0.75)],
                  dtype=[('I', 'S1'), ('A', '<i8'), ('B', '<f8')])
        """
if index:
    ix_vals = [
        np.asarray(self.index.get_level_values(i))
        for i in range(self.index.nlevels)
    ]

    arrays = ix_vals + [
        np.asarray(self.iloc[:, i]) for i in range(len(self.columns))
    ]

    index_names = list(self.index.names)

    if isinstance(self.index, MultiIndex):
        index_names = com.fill_missing_names(index_names)
    elif index_names[0] is None:
        index_names = ["index"]

    names = [str(name) for name in itertools.chain(index_names, self.columns)]
else:
    arrays = [np.asarray(self.iloc[:, i]) for i in range(len(self.columns))]
    names = [str(c) for c in self.columns]
    index_names = []

index_len = len(index_names)
formats = []

for i, v in enumerate(arrays):
    index_int = i

    # When the names and arrays are collected, we
    # first collect those in the DataFrame's index,
    # followed by those in its columns.
    #
    # Thus, the total length of the array is:
    # len(index_names) + len(DataFrame.columns).
    #
    # This check allows us to see whether we are
    # handling a name / array in the index or column.
    if index_int < index_len:
        dtype_mapping = index_dtypes
        name = index_names[index_int]
    else:
        index_int -= index_len
        dtype_mapping = column_dtypes
        name = self.columns[index_int]

    # We have a dictionary, so we get the data type
    # associated with the index or column (which can
    # be denoted by its name in the DataFrame or its
    # position in DataFrame's array of indices or
    # columns, whichever is applicable.
    if is_dict_like(dtype_mapping):
        if name in dtype_mapping:
            dtype_mapping = dtype_mapping[name]
        elif index_int in dtype_mapping:
            dtype_mapping = dtype_mapping[index_int]
        else:
            dtype_mapping = None

            # If no mapping can be found, use the array's
            # dtype attribute for formatting.
            #
            # A valid dtype must either be a type or
            # string naming a type.
    if dtype_mapping is None:
        formats.append(v.dtype)
    elif isinstance(dtype_mapping, (type, np.dtype, str)):
        # error: Argument 1 to "append" of "list" has incompatible
        # type "Union[type, dtype[Any], str]"; expected "dtype[Any]"
        formats.append(dtype_mapping)  # type: ignore[arg-type]
    else:
        element = "row" if i < index_len else "column"
        msg = f"Invalid dtype {dtype_mapping} specified for {element} {name}"
        raise ValueError(msg)

exit(np.rec.fromarrays(arrays, dtype={"names": names, "formats": formats}))
