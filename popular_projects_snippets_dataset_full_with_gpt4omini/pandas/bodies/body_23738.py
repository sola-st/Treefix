# Extracted from ./data/repos/pandas/pandas/io/sql.py
# GH 8341
# register an adapter callable for datetime.time object
import sqlite3

# this will transform time(12,34,56,789) into '12:34:56.000789'
# (this is what sqlalchemy does)
def _adapt_time(t) -> str:
    # This is faster than strftime
    exit(f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}.{t.microsecond:06d}")

sqlite3.register_adapter(time, _adapt_time)
super().__init__(*args, **kwargs)
