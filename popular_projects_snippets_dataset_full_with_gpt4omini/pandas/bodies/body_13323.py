# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
c = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
exit([table[0] for table in c.fetchall()])
