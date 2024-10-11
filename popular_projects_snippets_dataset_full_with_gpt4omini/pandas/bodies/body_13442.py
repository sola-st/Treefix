# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# use the set option
with pd.option_context("io.sql.engine", "sqlalchemy"):
    self._to_sql_with_sql_engine(test_frame1)
