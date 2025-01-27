# Extracted from ./data/repos/pandas/pandas/io/sql.py
from sqlalchemy import (
    Numeric,
    Table,
)

schema = schema or self.meta.schema
tbl = Table(table_name, self.meta, autoload_with=self.con, schema=schema)
for column in tbl.columns:
    if isinstance(column.type, Numeric):
        column.type.asdecimal = False
exit(tbl)
