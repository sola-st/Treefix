# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Write the contained data to an HDF5 file using HDFStore.

        Hierarchical Data Format (HDF) is self-describing, allowing an
        application to interpret the structure and contents of a file with
        no outside information. One HDF file can hold a mix of related objects
        which can be accessed as a group or as individual objects.

        In order to add another DataFrame or Series to an existing HDF file
        please use append mode and a different a key.

        .. warning::

           One can store a subclass of ``DataFrame`` or ``Series`` to HDF5,
           but the type of the subclass is lost upon storing.

        For more information see the :ref:`user guide <io.hdf5>`.

        Parameters
        ----------
        path_or_buf : str or pandas.HDFStore
            File path or HDFStore object.
        key : str
            Identifier for the group in the store.
        mode : {'a', 'w', 'r+'}, default 'a'
            Mode to open file:

            - 'w': write, a new file is created (an existing file with
              the same name would be deleted).
            - 'a': append, an existing file is opened for reading and
              writing, and if the file does not exist it is created.
            - 'r+': similar to 'a', but the file must already exist.
        complevel : {0-9}, default None
            Specifies a compression level for data.
            A value of 0 or None disables compression.
        complib : {'zlib', 'lzo', 'bzip2', 'blosc'}, default 'zlib'
            Specifies the compression library to be used.
            As of v0.20.2 these additional compressors for Blosc are supported
            (default if no compressor specified: 'blosc:blosclz'):
            {'blosc:blosclz', 'blosc:lz4', 'blosc:lz4hc', 'blosc:snappy',
            'blosc:zlib', 'blosc:zstd'}.
            Specifying a compression library which is not available issues
            a ValueError.
        append : bool, default False
            For Table formats, append the input data to the existing.
        format : {'fixed', 'table', None}, default 'fixed'
            Possible values:

            - 'fixed': Fixed format. Fast writing/reading. Not-appendable,
              nor searchable.
            - 'table': Table format. Write as a PyTables Table structure
              which may perform worse but allow more flexible operations
              like searching / selecting subsets of the data.
            - If None, pd.get_option('io.hdf.default_format') is checked,
              followed by fallback to "fixed".
        index : bool, default True
            Write DataFrame index as a column.
        min_itemsize : dict or int, optional
            Map column names to minimum string sizes for columns.
        nan_rep : Any, optional
            How to represent null values as str.
            Not allowed with append=True.
        dropna : bool, default False, optional
            Remove missing values.
        data_columns : list of columns or True, optional
            List of columns to create as indexed data columns for on-disk
            queries, or True to use all columns. By default only the axes
            of the object are indexed. See
            :ref:`Query via data columns<io.hdf5-query-data-columns>`. for
            more information.
            Applicable only to format='table'.
        errors : str, default 'strict'
            Specifies how encoding and decoding errors are to be handled.
            See the errors argument for :func:`open` for a full list
            of options.
        encoding : str, default "UTF-8"

        See Also
        --------
        read_hdf : Read from HDF file.
        DataFrame.to_orc : Write a DataFrame to the binary orc format.
        DataFrame.to_parquet : Write a DataFrame to the binary parquet format.
        DataFrame.to_sql : Write to a SQL table.
        DataFrame.to_feather : Write out feather-format for DataFrames.
        DataFrame.to_csv : Write out to a csv file.

        Examples
        --------
        >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]},
        ...                   index=['a', 'b', 'c'])  # doctest: +SKIP
        >>> df.to_hdf('data.h5', key='df', mode='w')  # doctest: +SKIP

        We can add another object to the same file:

        >>> s = pd.Series([1, 2, 3, 4])  # doctest: +SKIP
        >>> s.to_hdf('data.h5', key='s')  # doctest: +SKIP

        Reading from HDF file:

        >>> pd.read_hdf('data.h5', 'df')  # doctest: +SKIP
        A  B
        a  1  4
        b  2  5
        c  3  6
        >>> pd.read_hdf('data.h5', 's')  # doctest: +SKIP
        0    1
        1    2
        2    3
        3    4
        dtype: int64
        """
from pandas.io import pytables

# Argument 3 to "to_hdf" has incompatible type "NDFrame"; expected
# "Union[DataFrame, Series]" [arg-type]
pytables.to_hdf(
    path_or_buf,
    key,
    self,  # type: ignore[arg-type]
    mode=mode,
    complevel=complevel,
    complib=complib,
    append=append,
    format=format,
    index=index,
    min_itemsize=min_itemsize,
    nan_rep=nan_rep,
    dropna=dropna,
    data_columns=data_columns,
    errors=errors,
    encoding=encoding,
)
