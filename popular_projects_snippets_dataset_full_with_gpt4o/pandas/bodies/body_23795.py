# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Store object in HDFStore.

        Parameters
        ----------
        key : str
        value : {Series, DataFrame}
        format : 'fixed(f)|table(t)', default is 'fixed'
            Format to use when storing object in HDFStore. Value can be one of:

            ``'fixed'``
                Fixed format.  Fast writing/reading. Not-appendable, nor searchable.
            ``'table'``
                Table format.  Write as a PyTables Table structure which may perform
                worse but allow more flexible operations like searching / selecting
                subsets of the data.
        index : bool, default True
            Write DataFrame index as a column.
        append : bool, default False
            This will force Table format, append the input data to the existing.
        data_columns : list of columns or True, default None
            List of columns to create as data columns, or True to use all columns.
            See `here
            <https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#query-via-data-columns>`__.
        encoding : str, default None
            Provide an encoding for strings.
        track_times : bool, default True
            Parameter is propagated to 'create_table' method of 'PyTables'.
            If set to False it enables to have the same h5 files (same hashes)
            independent on creation time.
        dropna : bool, default False, optional
            Remove missing values.

            .. versionadded:: 1.1.0
        """
if format is None:
    format = get_option("io.hdf.default_format") or "fixed"
format = self._validate_format(format)
self._write_to_group(
    key,
    value,
    format=format,
    index=index,
    append=append,
    complib=complib,
    complevel=complevel,
    min_itemsize=min_itemsize,
    nan_rep=nan_rep,
    data_columns=data_columns,
    encoding=encoding,
    errors=errors,
    track_times=track_times,
    dropna=dropna,
)
