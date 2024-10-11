# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
conn = request.getfixturevalue(conn)
with pandasSQL_builder(conn) as pandasSQL:
    pandasSQL.to_sql(test_frame1, "test_frame", method=method)
    assert pandasSQL.has_table("test_frame")
assert count_rows(conn, "test_frame") == len(test_frame1)
