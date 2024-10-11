import sqlite3 # pragma: no cover

def _get_valid_sqlite_name(name):# pragma: no cover
    return ''.join(c if c.isalnum() else '_' for c in name) # pragma: no cover
name = 'test_table' # pragma: no cover
self = type('Mock', (object,), {'execute': lambda self, query: print(f'Executed query: {query}')})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/sql.py
from l3.Runtime import _l_
drop_sql = f"DROP TABLE {_get_valid_sqlite_name(name)}"
_l_(18089)
self.execute(drop_sql)
_l_(18090)
