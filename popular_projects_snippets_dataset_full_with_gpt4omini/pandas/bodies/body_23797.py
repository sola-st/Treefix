# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Append to Table in file.

        Node must already exist and be Table format.

        Parameters
        ----------
        key : str
        value : {Series, DataFrame}
        format : 'table' is the default
            Format to use when storing object in HDFStore.  Value can be one of:

            ``'table'``
                Table format. Write as a PyTables Table structure which may perform
                worse but allow more flexible operations like searching / selecting
                subsets of the data.
        index : bool, default True
            Write DataFrame index as a column.
        append       : bool, default True
            Append the input data to the existing.
        data_columns : list of columns, or True, default None
            List of columns to create as indexed data columns for on-disk
            queries, or True to use all columns. By default only the axes
            of the object are indexed. See `here
            <https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#query-via-data-columns>`__.
        min_itemsize : dict of columns that specify minimum str sizes
        nan_rep      : str to use as str nan representation
        chunksize    : size to chunk the writing
        expectedrows : expected TOTAL row size of this table
        encoding     : default None, provide an encoding for str
        dropna : bool, default False, optional
            Do not write an ALL nan row to the store settable
            by the option 'io.hdf.dropna_table'.

        Notes
        -----
        Does *not* check if data being appended overlaps with existing
        data in the table, so be careful
        """
if columns is not None:
    raise TypeError(
        "columns is not a supported keyword in append, try data_columns"
    )

if dropna is None:
    dropna = get_option("io.hdf.dropna_table")
if format is None:
    format = get_option("io.hdf.default_format") or "table"
format = self._validate_format(format)
self._write_to_group(
    key,
    value,
    format=format,
    axes=axes,
    index=index,
    append=append,
    complib=complib,
    complevel=complevel,
    min_itemsize=min_itemsize,
    nan_rep=nan_rep,
    chunksize=chunksize,
    expectedrows=expectedrows,
    dropna=dropna,
    data_columns=data_columns,
    encoding=encoding,
    errors=errors,
)
