# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""
    Read SQL query or database table into a DataFrame.

    This function is a convenience wrapper around ``read_sql_table`` and
    ``read_sql_query`` (for backward compatibility). It will delegate
    to the specific function depending on the provided input. A SQL query
    will be routed to ``read_sql_query``, while a database table name will
    be routed to ``read_sql_table``. Note that the delegated function might
    have more specific notes about their functionality not listed here.

    Parameters
    ----------
    sql : str or SQLAlchemy Selectable (select or text object)
        SQL query to be executed or a table name.
    con : SQLAlchemy connectable, str, or sqlite3 connection
        Using SQLAlchemy makes it possible to use any DB supported by that
        library. If a DBAPI2 object, only sqlite3 is supported. The user is responsible
        for engine disposal and connection closure for the SQLAlchemy connectable; str
        connections are closed automatically. See
        `here <https://docs.sqlalchemy.org/en/13/core/connections.html>`_.
    index_col : str or list of str, optional, default: None
        Column(s) to set as index(MultiIndex).
    coerce_float : bool, default True
        Attempts to convert values of non-string, non-numeric objects (like
        decimal.Decimal) to floating point, useful for SQL result sets.
    params : list, tuple or dict, optional, default: None
        List of parameters to pass to execute method.  The syntax used
        to pass parameters is database driver dependent. Check your
        database driver documentation for which of the five syntax styles,
        described in PEP 249's paramstyle, is supported.
        Eg. for psycopg2, uses %(name)s so use params={'name' : 'value'}.
    parse_dates : list or dict, default: None
        - List of column names to parse as dates.
        - Dict of ``{column_name: format string}`` where format string is
          strftime compatible in case of parsing string times, or is one of
          (D, s, ns, ms, us) in case of parsing integer timestamps.
        - Dict of ``{column_name: arg dict}``, where the arg dict corresponds
          to the keyword arguments of :func:`pandas.to_datetime`
          Especially useful with databases without native Datetime support,
          such as SQLite.
    columns : list, default: None
        List of column names to select from SQL table (only used when reading
        a table).
    chunksize : int, default None
        If specified, return an iterator where `chunksize` is the
        number of rows to include in each chunk.
    use_nullable_dtypes : bool = False
        Whether to use nullable dtypes as default when reading data. If
        set to True, nullable dtypes are used for all dtypes that have a nullable
        implementation, even if no nulls are present.

        .. versionadded:: 2.0
    dtype : Type name or dict of columns
        Data type for data or columns. E.g. np.float64 or
        {‘a’: np.float64, ‘b’: np.int32, ‘c’: ‘Int64’}.
        The argument is ignored if a table is passed instead of a query.

        .. versionadded:: 2.0.0

    Returns
    -------
    DataFrame or Iterator[DataFrame]

    See Also
    --------
    read_sql_table : Read SQL database table into a DataFrame.
    read_sql_query : Read SQL query into a DataFrame.

    Examples
    --------
    Read data from SQL via either a SQL query or a SQL tablename.
    When using a SQLite database only SQL queries are accepted,
    providing only the SQL tablename will result in an error.

    >>> from sqlite3 import connect
    >>> conn = connect(':memory:')
    >>> df = pd.DataFrame(data=[[0, '10/11/12'], [1, '12/11/10']],
    ...                   columns=['int_column', 'date_column'])
    >>> df.to_sql('test_data', conn)
    2

    >>> pd.read_sql('SELECT int_column, date_column FROM test_data', conn)
       int_column date_column
    0           0    10/11/12
    1           1    12/11/10

    >>> pd.read_sql('test_data', 'postgres:///db_name')  # doctest:+SKIP

    Apply date parsing to columns through the ``parse_dates`` argument

    >>> pd.read_sql('SELECT int_column, date_column FROM test_data',
    ...             conn,
    ...             parse_dates=["date_column"])
       int_column date_column
    0           0  2012-10-11
    1           1  2010-12-11

    The ``parse_dates`` argument calls ``pd.to_datetime`` on the provided columns.
    Custom argument values for applying ``pd.to_datetime`` on a column are specified
    via a dictionary format:
    1. Ignore errors while parsing the values of "date_column"

    >>> pd.read_sql('SELECT int_column, date_column FROM test_data',
    ...             conn,
    ...             parse_dates={"date_column": {"errors": "ignore"}})
       int_column date_column
    0           0  2012-10-11
    1           1  2010-12-11

    2. Apply a dayfirst date parsing order on the values of "date_column"

    >>> pd.read_sql('SELECT int_column, date_column FROM test_data',
    ...             conn,
    ...             parse_dates={"date_column": {"dayfirst": True}})
       int_column date_column
    0           0  2012-11-10
    1           1  2010-11-12

    3. Apply custom formatting when date parsing the values of "date_column"

    >>> pd.read_sql('SELECT int_column, date_column FROM test_data',
    ...             conn,
    ...             parse_dates={"date_column": {"format": "%d/%m/%y"}})
       int_column date_column
    0           0  2012-11-10
    1           1  2010-11-12
    """
with pandasSQL_builder(con) as pandas_sql:

    if isinstance(pandas_sql, SQLiteDatabase):
        exit(pandas_sql.read_query(
            sql,
            index_col=index_col,
            params=params,
            coerce_float=coerce_float,
            parse_dates=parse_dates,
            chunksize=chunksize,
            use_nullable_dtypes=use_nullable_dtypes,
            dtype=dtype,
        ))

    try:
        _is_table_name = pandas_sql.has_table(sql)
    except Exception:
        # using generic exception to catch errors from sql drivers (GH24988)
        _is_table_name = False

    if _is_table_name:
        exit(pandas_sql.read_table(
            sql,
            index_col=index_col,
            coerce_float=coerce_float,
            parse_dates=parse_dates,
            columns=columns,
            chunksize=chunksize,
            use_nullable_dtypes=use_nullable_dtypes,
        ))
    else:
        exit(pandas_sql.read_query(
            sql,
            index_col=index_col,
            params=params,
            coerce_float=coerce_float,
            parse_dates=parse_dates,
            chunksize=chunksize,
            use_nullable_dtypes=use_nullable_dtypes,
            dtype=dtype,
        ))
