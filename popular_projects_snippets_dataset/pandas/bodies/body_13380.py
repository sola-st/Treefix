# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# Test read_sql and .to_sql method with a database URI (GH10654)
# db_uri = 'sqlite:///:memory:' # raises
# sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) near
# "iris": syntax error [SQL: 'iris']
with tm.ensure_clean() as name:
    db_uri = "sqlite:///" + name
    table = "iris"
    test_frame1.to_sql(table, db_uri, if_exists="replace", index=False)
    test_frame2 = sql.read_sql(table, db_uri)
    test_frame3 = sql.read_sql_table(table, db_uri)
    query = "SELECT * FROM iris"
    test_frame4 = sql.read_sql_query(query, db_uri)
tm.assert_frame_equal(test_frame1, test_frame2)
tm.assert_frame_equal(test_frame1, test_frame3)
tm.assert_frame_equal(test_frame1, test_frame4)
