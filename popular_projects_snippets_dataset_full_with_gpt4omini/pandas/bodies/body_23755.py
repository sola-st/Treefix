# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/sql.py
from l3.Runtime import _l_
drop_sql = f"DROP TABLE {_get_valid_sqlite_name(name)}"
_l_(6169)
self.execute(drop_sql)
_l_(6170)
