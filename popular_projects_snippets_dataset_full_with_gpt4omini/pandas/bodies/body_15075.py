# Extracted from ./data/repos/pandas/pandas/tests/base/test_misc.py
series = series_with_simple_index
total_usage = series.memory_usage(index=True)
non_index_usage = series.memory_usage(index=False)
index_usage = series.index.memory_usage()
assert total_usage == non_index_usage + index_usage
