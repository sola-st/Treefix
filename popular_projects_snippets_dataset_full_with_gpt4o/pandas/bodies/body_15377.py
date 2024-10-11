# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
ser = Series(np.random.randn(8), index=[2, 4, 6, 8, 10, 12, 14, 16])

ser[:4] = 0
assert (ser[:4] == 0).all()
assert not (ser[4:] == 0).any()
