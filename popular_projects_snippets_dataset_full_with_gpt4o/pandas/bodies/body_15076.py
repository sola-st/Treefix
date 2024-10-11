# Extracted from ./data/repos/pandas/pandas/tests/base/test_misc.py
series = tm.make_rand_series(name="a", dtype=dtype)
total_usage = series.memory_usage(index=True)
non_index_usage = series.memory_usage(index=False)
index_usage = series.index.memory_usage()
assert total_usage == non_index_usage + index_usage
