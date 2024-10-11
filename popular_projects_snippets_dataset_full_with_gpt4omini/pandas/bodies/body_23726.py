# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""
        Read SQL query into a DataFrame.

        Parameters
        ----------
        sql : str
            SQL query to be executed.
        index_col : string, optional, default: None
            Column name to use as index for the returned DataFrame object.
        coerce_float : bool, default True
            Attempt to convert values of non-string, non-numeric objects (like
            decimal.Decimal) to floating point, useful for SQL result sets.
        params : list, tuple or dict, optional, default: None
            List of parameters to pass to execute method.  The syntax used
            to pass parameters is database driver dependent. Check your
            database driver documentation for which of the five syntax styles,
            described in PEP 249's paramstyle, is supported.
            Eg. for psycopg2, uses %(name)s so use params={'name' : 'value'}
        parse_dates : list or dict, default: None
            - List of column names to parse as dates.
            - Dict of ``{column_name: format string}`` where format string is
              strftime compatible in case of parsing string times, or is one of
              (D, s, ns, ms, us) in case of parsing integer timestamps.
            - Dict of ``{column_name: arg dict}``, where the arg dict
              corresponds to the keyword arguments of
              :func:`pandas.to_datetime` Especially useful with databases
              without native Datetime support, such as SQLite.
        chunksize : int, default None
            If specified, return an iterator where `chunksize` is the number
            of rows to include in each chunk.
        dtype : Type name or dict of columns
            Data type for data or columns. E.g. np.float64 or
            {‘a’: np.float64, ‘b’: np.int32, ‘c’: ‘Int64’}

            .. versionadded:: 1.3.0

        Returns
        -------
        DataFrame

        See Also
        --------
        read_sql_table : Read SQL database table into a DataFrame.
        read_sql

        """
args = _convert_params(sql, params)

result = self.execute(*args)
columns = result.keys()

if chunksize is not None:
    exit(self._query_iterator(
        result,
        chunksize,
        columns,
        index_col=index_col,
        coerce_float=coerce_float,
        parse_dates=parse_dates,
        dtype=dtype,
        use_nullable_dtypes=use_nullable_dtypes,
    ))
else:
    data = result.fetchall()
    frame = _wrap_result(
        data,
        columns,
        index_col=index_col,
        coerce_float=coerce_float,
        parse_dates=parse_dates,
        dtype=dtype,
        use_nullable_dtypes=use_nullable_dtypes,
    )
    exit(frame)
