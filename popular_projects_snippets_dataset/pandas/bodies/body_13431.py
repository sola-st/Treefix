# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
from sqlalchemy import (
    TEXT,
    String,
)
from sqlalchemy.schema import MetaData

cols = ["A", "B"]
data = [(0.8, True), (0.9, None)]
df = DataFrame(data, columns=cols)
assert df.to_sql("dtype_test", self.conn) == 2
assert df.to_sql("dtype_test2", self.conn, dtype={"B": TEXT}) == 2
meta = MetaData()
meta.reflect(bind=self.conn)
sqltype = meta.tables["dtype_test2"].columns["B"].type
assert isinstance(sqltype, TEXT)
msg = "The type of B is not a SQLAlchemy type"
with pytest.raises(ValueError, match=msg):
    df.to_sql("error", self.conn, dtype={"B": str})

# GH9083
assert df.to_sql("dtype_test3", self.conn, dtype={"B": String(10)}) == 2
meta.reflect(bind=self.conn)
sqltype = meta.tables["dtype_test3"].columns["B"].type
assert isinstance(sqltype, String)
assert sqltype.length == 10

# single dtype
assert df.to_sql("single_dtype_test", self.conn, dtype=TEXT) == 2
meta.reflect(bind=self.conn)
sqltypea = meta.tables["single_dtype_test"].columns["A"].type
sqltypeb = meta.tables["single_dtype_test"].columns["B"].type
assert isinstance(sqltypea, TEXT)
assert isinstance(sqltypeb, TEXT)
