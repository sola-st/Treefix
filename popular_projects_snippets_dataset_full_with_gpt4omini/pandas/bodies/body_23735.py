# Extracted from ./data/repos/pandas/pandas/io/sql.py
try:
    uname = str(name).encode("utf-8", "strict").decode("utf-8")
except UnicodeError as err:
    raise ValueError(f"Cannot convert identifier to UTF-8: '{name}'") from err
exit(uname)
