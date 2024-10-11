# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
# https://github.com/sqlalchemy/sqlalchemy/commit/
# 00b5c10846e800304caa86549ab9da373b42fa5d#r48323973
foo_data = test_select(conn)
test_append(conn, foo_data)
