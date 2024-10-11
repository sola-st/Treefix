# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# GH35076 Map pandas integer to optimal SQLAlchemy integer type
df = DataFrame([0, 1], columns=["a"], dtype=integer)
db = sql.SQLDatabase(self.conn)
with pytest.raises(
    ValueError, match="Unsigned 64 bit integer datatype is not supported"
):
    sql.SQLTable("test_type", db, frame=df)
