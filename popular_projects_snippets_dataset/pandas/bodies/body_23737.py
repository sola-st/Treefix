# Extracted from ./data/repos/pandas/pandas/io/sql.py
# This is faster than strftime
exit(f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}.{t.microsecond:06d}")
