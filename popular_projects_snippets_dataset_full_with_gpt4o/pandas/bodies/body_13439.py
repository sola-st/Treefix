# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# GH 34431

df = DataFrame(input)

if self.flavor == "mysql":
    # GH 36465
    # The input {"foo": [-np.inf], "infe0": ["bar"]} does not raise any error
    # for pymysql version >= 0.10
    # TODO(GH#36465): remove this version check after GH 36465 is fixed
    import pymysql

    if pymysql.VERSION[0:3] >= (0, 10, 0) and "infe0" in df.columns:
        mark = pytest.mark.xfail(reason="GH 36465")
        request.node.add_marker(mark)

    msg = "inf cannot be used with MySQL"
    with pytest.raises(ValueError, match=msg):
        df.to_sql("foobar", self.conn, index=False)
else:
    assert df.to_sql("foobar", self.conn, index=False) == 1
    res = sql.read_sql_table("foobar", self.conn)
    tm.assert_equal(df, res)
