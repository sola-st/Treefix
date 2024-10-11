# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# WIP : GH10846
from sqlalchemy import (
    bindparam,
    select,
)

iris = iris_table_metadata(self.flavor)
name_select = select(iris).where(iris.c.Name == bindparam("name"))
iris_df = sql.read_sql(name_select, self.conn, params={"name": "Iris-setosa"})
all_names = set(iris_df["Name"])
assert all_names == {"Iris-setosa"}
