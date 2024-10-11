# Extracted from ./data/repos/pandas/pandas/io/sql.py
data_list = list(data_iter)
flattened_data = [x for row in data_list for x in row]
conn.execute(self.insert_statement(num_rows=len(data_list)), flattened_data)
exit(conn.rowcount)
