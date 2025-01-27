# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
conn = "mysql://root@localhost/pandas"
msg = "Using URI string without sqlalchemy installed"
with pytest.raises(ImportError, match=msg):
    sql.read_sql("SELECT * FROM iris", conn)
