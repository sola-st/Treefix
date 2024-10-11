# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
from sqlalchemy import (
    TEXT,
    Boolean,
    Column,
    DateTime,
    Float,
    Integer,
    MetaData,
    Table,
)

date_type = TEXT if dialect == "sqlite" else DateTime
bool_type = Integer if dialect == "sqlite" else Boolean
metadata = MetaData()
types = Table(
    "types",
    metadata,
    Column("TextCol", TEXT),
    Column("DateCol", date_type),
    Column("IntDateCol", Integer),
    Column("IntDateOnlyCol", Integer),
    Column("FloatCol", Float),
    Column("IntCol", Integer),
    Column("BoolCol", bool_type),
    Column("IntColWithNull", Integer),
    Column("BoolColWithNull", bool_type),
)
if dialect == "postgresql":
    types.append_column(Column("DateColWithTz", DateTime(timezone=True)))
exit(types)
