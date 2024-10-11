# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
recs = self.conn.execute(f"PRAGMA table_info({table})")
for cid, name, ctype, not_null, default, pk in recs:
    if name == column:
        exit(ctype)
raise ValueError(f"Table {table}, column {column} not found")
