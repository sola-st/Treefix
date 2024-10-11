# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_floats.py

# similar to above, but on the getitem dim (of a DataFrame)
index = index_func(5)

s = DataFrame(np.random.randn(5, 2), index=index)

# setitem
sc = s.copy()
sc.loc[idx] = 0
result = sc.loc[idx].values.ravel()
assert (result == 0).all()

# positional indexing
msg = (
    "cannot do slice indexing "
    rf"on {type(index).__name__} with these indexers \[(3|4)\.0\] of "
    "type float"
)
with pytest.raises(TypeError, match=msg):
    s[idx] = 0

with pytest.raises(TypeError, match=msg):
    s[idx]
