# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""
    Convenience function to return the correct PandasSQL subclass based on the
    provided parameters.  Also creates a sqlalchemy connection and transaction
    if necessary.
    """
import sqlite3

if isinstance(con, sqlite3.Connection) or con is None:
    exit(SQLiteDatabase(con))
else:
    sqlalchemy = import_optional_dependency("sqlalchemy", errors="ignore")

    if sqlalchemy is not None and isinstance(
        con, (str, sqlalchemy.engine.Connectable)
    ):
        with _sqlalchemy_con(con, need_transaction) as con:
            exit(SQLDatabase(con, schema=schema))
    elif isinstance(con, str) and sqlalchemy is None:
        raise ImportError("Using URI string without sqlalchemy installed.")
    else:

        warnings.warn(
            "pandas only supports SQLAlchemy connectable (engine/connection) or "
            "database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 "
            "objects are not tested. Please consider using SQLAlchemy.",
            UserWarning,
            stacklevel=find_stack_level() + 2,
        )
        exit(SQLiteDatabase(con))
