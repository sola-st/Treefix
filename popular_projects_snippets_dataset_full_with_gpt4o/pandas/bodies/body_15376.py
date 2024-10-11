# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
ser = Series(range(10), index=list(range(10)))
ser[-12:] = 0
assert (ser == 0).all()

ser[:-12] = 5
assert (ser == 0).all()
