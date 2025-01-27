# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
create_sql = """
        CREATE TABLE test
        (
        a TEXT,
        b TEXT,
        c REAL,
        PRIMARY KEY (a, b)
        );
        """
with contextlib.closing(sqlite3.connect(":memory:")) as conn:
    cur = conn.cursor()
    cur.execute(create_sql)

    with sql.pandasSQL_builder(conn) as pandas_sql:
        pandas_sql.execute('INSERT INTO test VALUES("foo", "bar", 1.234)')

msg = "Cannot operate on a closed database."
with pytest.raises(sqlite3.ProgrammingError, match=msg):
    tquery("select * from test", con=conn)
