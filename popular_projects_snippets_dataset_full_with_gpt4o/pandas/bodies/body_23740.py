# Extracted from ./data/repos/pandas/pandas/io/sql.py
with self.pd_sql.run_transaction() as conn:
    for stmt in self.table:
        conn.execute(stmt)
