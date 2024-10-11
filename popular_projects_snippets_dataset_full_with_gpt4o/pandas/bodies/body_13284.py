# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
from sqlalchemy import (
    REAL,
    Column,
    Float,
    MetaData,
    String,
    Table,
)

dtype = Float if dialect == "postgresql" else REAL
metadata = MetaData()
iris = Table(
    "iris",
    metadata,
    Column("SepalLength", dtype),
    Column("SepalWidth", dtype),
    Column("PetalLength", dtype),
    Column("PetalWidth", dtype),
    Column("Name", String(200)),
)
exit(iris)
