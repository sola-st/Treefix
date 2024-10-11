# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
with self.pandasSQL.run_transaction() as trans:
    stmt = "CREATE TABLE test_trans (A INT, B TEXT)"
    if isinstance(self.pandasSQL, SQLiteDatabase):
        trans.execute(stmt)
    else:
        from sqlalchemy import text

        stmt = text(stmt)
        trans.execute(stmt)

class DummyException(Exception):
    pass

# Make sure when transaction is rolled back, no rows get inserted
ins_sql = "INSERT INTO test_trans (A,B) VALUES (1, 'blah')"
if isinstance(self.pandasSQL, SQLDatabase):
    from sqlalchemy import text

    ins_sql = text(ins_sql)
try:
    with self.pandasSQL.run_transaction() as trans:
        trans.execute(ins_sql)
        raise DummyException("error")
except DummyException:
    # ignore raised exception
    pass
res = self.pandasSQL.read_query("SELECT * FROM test_trans")
assert len(res) == 0

# Make sure when transaction is committed, rows do get inserted
with self.pandasSQL.run_transaction() as trans:
    trans.execute(ins_sql)
res2 = self.pandasSQL.read_query("SELECT * FROM test_trans")
assert len(res2) == 1
