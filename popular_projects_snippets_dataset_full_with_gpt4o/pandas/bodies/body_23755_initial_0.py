import sqlite3 # pragma: no cover

def _get_valid_sqlite_name(name): return name.replace(' ', '_') # pragma: no cover
name = 'test_table' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/sql.py
from l3.Runtime import _l_
drop_sql = f"DROP TABLE {_get_valid_sqlite_name(name)}"
_l_(18089)
self.execute(drop_sql)
_l_(18090)
