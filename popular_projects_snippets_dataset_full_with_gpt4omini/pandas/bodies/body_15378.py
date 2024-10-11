# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# caught this bug when writing tests
series = Series(tm.makeIntIndex(20).astype(float), index=tm.makeIntIndex(20))

series[::2] = 0
assert (series[::2] == 0).all()
