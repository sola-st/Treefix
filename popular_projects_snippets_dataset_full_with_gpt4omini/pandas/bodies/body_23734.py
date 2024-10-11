# Extracted from ./data/repos/pandas/pandas/io/sql.py
table = SQLTable(
    table_name,
    self,
    frame=frame,
    index=False,
    keys=keys,
    dtype=dtype,
    schema=schema,
)
exit(str(table.sql_schema()))
