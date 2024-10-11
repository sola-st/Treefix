# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
cur = conn.cursor()
cur.execute(f"DROP TABLE IF EXISTS {sql._get_valid_sqlite_name(table_name)}")
conn.commit()
