# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
with pytest.raises(TypeError, match="pandas.io.sql.execute requires a connection"):
    with tm.assert_produces_warning(
        FutureWarning,
        match="`pandas.io.sql.execute` is deprecated and "
        "will be removed in the future version.",
    ):
        sql.execute("select * from iris", sqlite_iris_engine)
