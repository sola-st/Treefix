# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
conn = request.getfixturevalue(conn)
with pandasSQL_builder(conn) as pandasSQL:
    pandasSQL.to_sql(test_frame1, "test_frame", if_exists="fail")
    pandasSQL.to_sql(test_frame1, "test_frame", if_exists=mode)
    assert pandasSQL.has_table("test_frame")
assert count_rows(conn, "test_frame") == num_row_coef * len(test_frame1)
