# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""
    Read SQL database table into a DataFrame.

    Given a table name and a SQLAlchemy connectable, returns a DataFrame.
    This function does not support DBAPI connections.

    Parameters
    ----------
    table_name : str
        Name of SQL table in database.
    con : SQLAlchemy connectable or str
        A database URI could be provided as str.
        SQLite DBAPI connection mode not supported.
    schema : str, default None
        Name of SQL schema in database to query (if database flavor
        supports this). Uses default schema if None (default).
    index_col : str or list of str, optional, default: None
        Column(s) to set as index(MultiIndex).
    coerce_float : bool, default True
        Attempts to convert values of non-string, non-numeric objects (like
        decimal.Decimal) to floating point. Can result in loss of Precision.
    parse_dates : list or dict, default None
        - List of column names to parse as dates.
        - Dict of ``{column_name: format string}`` where format string is
          strftime compatible in case of parsing string times or is one of
          (D, s, ns, ms, us) in case of parsing integer timestamps.
        - Dict of ``{column_name: arg dict}``, where the arg dict corresponds
          to the keyword arguments of :func:`pandas.to_datetime`
          Especially useful with databases without native Datetime support,
          such as SQLite.
    columns : list, default None
        List of column names to select from SQL table.
    chunksize : int, default None
        If specified, returns an iterator where `chunksize` is the number of
        rows to include in each chunk.
    use_nullable_dtypes : bool = False
        Whether to use nullable dtypes as default when reading data. If
        set to True, nullable dtypes are used for all dtypes that have a nullable
        implementation, even if no nulls are present.

        .. versionadded:: 2.0

    Returns
    -------
    DataFrame or Iterator[DataFrame]
        A SQL table is returned as two-dimensional data structure with labeled
        axes.

    See Also
    --------
    read_sql_query : Read SQL query into a DataFrame.
    read_sql : Read SQL query or database table into a DataFrame.

    Notes
    -----
    Any datetime values with time zone information will be converted to UTC.

    Examples
    --------
    >>> pd.read_sql_table('table_name', 'postgres:///db_name')  # doctest:+SKIP
    """
with pandasSQL_builder(con, schema=schema) as pandas_sql:
    if not pandas_sql.has_table(table_name):
        raise ValueError(f"Table {table_name} not found")

    table = pandas_sql.read_table(
        table_name,
        index_col=index_col,
        coerce_float=coerce_float,
        parse_dates=parse_dates,
        columns=columns,
        chunksize=chunksize,
        use_nullable_dtypes=use_nullable_dtypes,
    )

if table is not None:
    exit(table)
else:
    raise ValueError(f"Table {table_name} not found", con)
