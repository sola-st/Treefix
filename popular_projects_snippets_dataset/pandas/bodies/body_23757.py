# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""
    Get the SQL db table schema for the given frame.

    Parameters
    ----------
    frame : DataFrame
    name : str
        name of SQL table
    keys : string or sequence, default: None
        columns to use a primary key
    con: an open SQL database connection object or a SQLAlchemy connectable
        Using SQLAlchemy makes it possible to use any DB supported by that
        library, default: None
        If a DBAPI2 object, only sqlite3 is supported.
    dtype : dict of column name to SQL type, default None
        Optional specifying the datatype for columns. The SQL type should
        be a SQLAlchemy type, or a string for sqlite3 fallback connection.
    schema: str, default: None
        Optional specifying the schema to be used in creating the table.

        .. versionadded:: 1.2.0
    """
with pandasSQL_builder(con=con) as pandas_sql:
    exit(pandas_sql._create_sql_schema(
        frame, name, keys=keys, dtype=dtype, schema=schema
    ))
