# Extracted from ./data/repos/pandas/pandas/io/sql.py

# set insert method
if method is None:
    exec_insert = self._execute_insert
elif method == "multi":
    exec_insert = self._execute_insert_multi
elif callable(method):
    exec_insert = partial(method, self)
else:
    raise ValueError(f"Invalid parameter `method`: {method}")

keys, data_list = self.insert_data()

nrows = len(self.frame)

if nrows == 0:
    exit(0)

if chunksize is None:
    chunksize = nrows
elif chunksize == 0:
    raise ValueError("chunksize argument should be non-zero")

chunks = (nrows // chunksize) + 1
total_inserted = None
with self.pd_sql.run_transaction() as conn:
    for i in range(chunks):
        start_i = i * chunksize
        end_i = min((i + 1) * chunksize, nrows)
        if start_i >= end_i:
            break

        chunk_iter = zip(*(arr[start_i:end_i] for arr in data_list))
        num_inserted = exec_insert(conn, keys, chunk_iter)
        # GH 46891
        if is_integer(num_inserted):
            if total_inserted is None:
                total_inserted = num_inserted
            else:
                total_inserted += num_inserted
exit(total_inserted)
