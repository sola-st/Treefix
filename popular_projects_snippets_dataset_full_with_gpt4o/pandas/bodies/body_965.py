# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_floats.py

# GH 4892
# float_indexers should raise exceptions
# on appropriate Index types & accessors

i = index_func(5)
s = gen_obj(frame_or_series, i)

# getting
with pytest.raises(KeyError, match="^3.0$"):
    indexer_sl(s)[3.0]

# contains
assert 3.0 not in s

s2 = s.copy()
indexer_sl(s2)[3.0] = 10

if indexer_sl is tm.setitem:
    assert 3.0 in s2.axes[-1]
elif indexer_sl is tm.loc:
    assert 3.0 in s2.axes[0]
else:
    assert 3.0 not in s2.axes[0]
    assert 3.0 not in s2.axes[-1]
