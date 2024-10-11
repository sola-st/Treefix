# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""
    Check if DataBase has named table.

    Parameters
    ----------
    table_name: string
        Name of SQL table.
    con: SQLAlchemy connectable(engine/connection) or sqlite3 DBAPI2 connection
        Using SQLAlchemy makes it possible to use any DB supported by that
        library.
        If a DBAPI2 object, only sqlite3 is supported.
    schema : string, default None
        Name of SQL schema in database to write to (if database flavor supports
        this). If None, use default schema (default).

    Returns
    -------
    boolean
    """
with pandasSQL_builder(con, schema=schema) as pandas_sql:
    exit(pandas_sql.has_table(table_name))
