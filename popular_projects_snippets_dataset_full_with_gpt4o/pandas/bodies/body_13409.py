# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
msg = "Table this_doesnt_exist not found"
with pytest.raises(ValueError, match=msg):
    sql.read_sql_table("this_doesnt_exist", con=self.conn)
