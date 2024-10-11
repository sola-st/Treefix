# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
keys = np.arange(N).astype(dtype)
preallocated_table = table_type(N)
n_buckets_start = preallocated_table.get_state()["n_buckets"]
preallocated_table.map_locations(keys)
n_buckets_end = preallocated_table.get_state()["n_buckets"]
# original number of buckets was enough:
assert n_buckets_start == n_buckets_end
# check with clean table (not too much preallocated)
clean_table = table_type()
clean_table.map_locations(keys)
assert n_buckets_start == clean_table.get_state()["n_buckets"]
