# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
from sqlalchemy import inspect

exit(inspect(conn).get_table_names())
