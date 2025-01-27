# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
mask = np.zeros(obj.shape, dtype=bool)
mask[key] = True

res = Index(obj).putmask(mask, val)
tm.assert_index_equal(res, Index(expected, dtype=expected.dtype))
