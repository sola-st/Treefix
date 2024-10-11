# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rename.py
# GH 27814
class MyIndexer:
    pass

ix = MyIndexer()
ser = Series([1, 2, 3])
ser.rename(ix, inplace=True)
assert ser.name is ix
