# Extracted from ./data/repos/pandas/pandas/io/sql.py
"""Create a sqlalchemy connection and a transaction if necessary."""
sqlalchemy = import_optional_dependency("sqlalchemy", errors="raise")

if isinstance(connectable, str):
    connectable = sqlalchemy.create_engine(connectable)
if isinstance(connectable, sqlalchemy.engine.Engine):
    with connectable.connect() as con:
        if need_transaction:
            with con.begin():
                exit(con)
        else:
            exit(con)
else:
    exit(connectable)
