# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    Integer,
)
from sqlalchemy.schema import MetaData

cols = {
    "Bool": Series([True, None]),
    "Date": Series([datetime(2012, 5, 1), None]),
    "Int": Series([1, None], dtype="object"),
    "Float": Series([1.1, None]),
}
df = DataFrame(cols)

tbl = "notna_dtype_test"
assert df.to_sql(tbl, self.conn) == 2
_ = sql.read_sql_table(tbl, self.conn)
meta = MetaData()
meta.reflect(bind=self.conn)
my_type = Integer if self.flavor == "mysql" else Boolean
col_dict = meta.tables[tbl].columns
assert isinstance(col_dict["Bool"].type, my_type)
assert isinstance(col_dict["Date"].type, DateTime)
assert isinstance(col_dict["Int"].type, Integer)
assert isinstance(col_dict["Float"].type, Float)
