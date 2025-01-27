# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
mask = np.zeros(obj.shape, dtype=bool)
mask[key] = True

res = Index(obj).where(~mask, val)
expected_idx = Index(expected, dtype=expected.dtype)
tm.assert_index_equal(res, expected_idx)
