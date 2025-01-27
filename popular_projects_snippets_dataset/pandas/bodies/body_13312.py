# Extracted from ./data/repos/pandas/pandas/tests/io/test_sql.py
check.append(1)
data = [dict(zip(keys, row)) for row in data_iter]
conn.execute(pd_table.table.insert(), data)
