# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
conn = request.getfixturevalue(conn)
with pandasSQL_builder(conn) as pandasSQL:
    pandasSQL.to_sql(test_frame1, "test_frame", if_exists="fail")
    assert pandasSQL.has_table("test_frame")

    msg = "Table 'test_frame' already exists"
    with pytest.raises(ValueError, match=msg):
        pandasSQL.to_sql(test_frame1, "test_frame", if_exists="fail")
