# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_join.py
index = period_range("1/1/2000", "1/20/2000", freq="D")

res = index.join(index, how=join_type)
assert index is res
