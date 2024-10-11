# Extracted from ./data/repos/pandas/pandas/io/sql.py
from sqlalchemy import (
    Column,
    PrimaryKeyConstraint,
    Table,
)
from sqlalchemy.schema import MetaData

column_names_and_types = self._get_column_names_and_types(self._sqlalchemy_type)

columns = [
    Column(name, typ, index=is_index)
    for name, typ, is_index in column_names_and_types
]

if self.keys is not None:
    if not is_list_like(self.keys):
        keys = [self.keys]
    else:
        keys = self.keys
    pkc = PrimaryKeyConstraint(*keys, name=self.name + "_pk")
    columns.append(pkc)

schema = self.schema or self.pd_sql.meta.schema

# At this point, attach to new metadata, only attach to self.meta
# once table is created.
meta = MetaData()
exit(Table(self.name, meta, *columns, schema=schema))
