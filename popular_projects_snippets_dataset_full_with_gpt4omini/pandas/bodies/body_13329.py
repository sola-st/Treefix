# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
if self.flavor != "postgresql":
    for entry in types_data:
        entry.pop("DateColWithTz")
if isinstance(self.conn, sqlite3.Connection):
    types_data = [tuple(entry.values()) for entry in types_data]
    create_and_load_types_sqlite3(self.conn, types_data)
else:
    create_and_load_types(self.conn, types_data, self.flavor)
