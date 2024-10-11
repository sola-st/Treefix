# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
msg = "engine must be one of 'auto', 'sqlalchemy'"
with pytest.raises(ValueError, match=msg):
    self._to_sql_with_sql_engine(test_frame1, "bad_engine")
