# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""
    Execute the given SQL query using the provided connection object.

    Parameters
    ----------
    sql : string
        SQL query to be executed.
    con : SQLAlchemy connection or sqlite3 connection
        If a DBAPI2 object, only sqlite3 is supported.
    params : list or tuple, optional, default: None
        List of parameters to pass to execute method.

    Returns
    -------
    Results Iterable
    """
warnings.warn(
    "`pandas.io.sql.execute` is deprecated and "
    "will be removed in the future version.",
    FutureWarning,
    stacklevel=find_stack_level(),
)  # GH50185
sqlalchemy = import_optional_dependency("sqlalchemy", errors="ignore")

if sqlalchemy is not None and isinstance(con, (str, sqlalchemy.engine.Engine)):
    raise TypeError("pandas.io.sql.execute requires a connection")  # GH50185
with pandasSQL_builder(con, need_transaction=True) as pandas_sql:
    args = _convert_params(sql, params)
    exit(pandas_sql.execute(*args))
