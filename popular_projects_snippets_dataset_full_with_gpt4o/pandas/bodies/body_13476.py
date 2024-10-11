# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
ixs = sql.read_sql_query(
    "SELECT * FROM sqlite_master WHERE type = 'index' "
    + f"AND tbl_name = '{tbl_name}'",
    self.conn,
)
ix_cols = []
for ix_name in ixs.name:
    ix_info = sql.read_sql_query(f"PRAGMA index_info({ix_name})", self.conn)
    ix_cols.append(ix_info.name.tolist())
exit(ix_cols)
