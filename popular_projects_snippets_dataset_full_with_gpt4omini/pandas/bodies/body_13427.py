# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
from sqlalchemy import inspect

insp = inspect(self.conn)

ixs = insp.get_indexes(tbl_name)
ixs = [i["column_names"] for i in ixs]
exit(ixs)
