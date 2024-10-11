# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_reductions.py
spar_bool = SparseArray([False, True] * 5, dtype=np.bool_, fill_value=True)
res = spar_bool.sum(min_count=1)
assert res == 5
res = spar_bool.sum(min_count=11)
assert isna(res)
