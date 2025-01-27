# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# WIP : GH10846
from sqlalchemy import text

name_text = text("select * from iris where name=:name")
iris_df = sql.read_sql(name_text, self.conn, params={"name": "Iris-versicolor"})
all_names = set(iris_df["Name"])
assert all_names == {"Iris-versicolor"}
