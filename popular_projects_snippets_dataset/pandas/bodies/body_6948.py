# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
# GH 23525
idx1 = idx_fact1(10)
idx2 = idx_fact2(20)

res1 = idx1.union(idx2)
res2 = idx2.union(idx1)

assert res1.dtype in (idx1.dtype, idx2.dtype)
assert res2.dtype in (idx1.dtype, idx2.dtype)
