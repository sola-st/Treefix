# Extracted from ./data/repos/pandas/pandas/io/sql.py
data_list = list(data_iter)
conn.executemany(self.insert_statement(num_rows=1), data_list)
exit(conn.rowcount)
