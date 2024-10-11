# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
conn = request.getfixturevalue(conn)

check = []  # used to double check function below is really being used

def sample(pd_table, conn, keys, data_iter):
    check.append(1)
    data = [dict(zip(keys, row)) for row in data_iter]
    conn.execute(pd_table.table.insert(), data)

with pandasSQL_builder(conn) as pandasSQL:
    pandasSQL.to_sql(test_frame1, "test_frame", method=sample)
    assert pandasSQL.has_table("test_frame")
assert check == [1]
assert count_rows(conn, "test_frame") == len(test_frame1)
