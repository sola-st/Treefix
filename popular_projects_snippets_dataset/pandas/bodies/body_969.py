# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_floats.py
getitem = indexer_sl is not tm.loc

# test how scalar float indexers work on int indexes

# integer index
i = index_func(5)
obj = gen_obj(frame_or_series, i)

# coerce to equal int

result = indexer_sl(obj)[3.0]
self.check(result, obj, 3, getitem)

if isinstance(obj, Series):

    def compare(x, y):
        assert x == y

    expected = 100
else:
    compare = tm.assert_series_equal
    if getitem:
        expected = Series(100, index=range(len(obj)), name=3)
    else:
        expected = Series(100.0, index=range(len(obj)), name=3)

s2 = obj.copy()
indexer_sl(s2)[3.0] = 100

result = indexer_sl(s2)[3.0]
compare(result, expected)

result = indexer_sl(s2)[3]
compare(result, expected)
