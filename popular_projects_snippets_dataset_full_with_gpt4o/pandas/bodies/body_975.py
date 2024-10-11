# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_floats.py

# similar to above, but on the getitem dim (of a DataFrame)
index = index_func(5)

s = DataFrame(np.random.randn(5, 2), index=index)

# getitem
for idx in [slice(0.0, 1), slice(0, 1.0), slice(0.0, 1.0)]:

    result = s.loc[idx]
    indexer = slice(0, 2)
    self.check(result, s, indexer, False)

    # positional indexing
    msg = (
        "cannot do slice indexing "
        rf"on {type(index).__name__} with these indexers \[(0|1)\.0\] of "
        "type float"
    )
    with pytest.raises(TypeError, match=msg):
        s[idx]

        # getitem out-of-bounds
for idx in [slice(-10, 10), slice(-10.0, 10.0)]:

    result = s.loc[idx]
    self.check(result, s, slice(-10, 10), True)

# positional indexing
msg = (
    "cannot do slice indexing "
    rf"on {type(index).__name__} with these indexers \[-10\.0\] of "
    "type float"
)
with pytest.raises(TypeError, match=msg):
    s[slice(-10.0, 10.0)]

# getitem odd floats
for idx, res in [
    (slice(0.5, 1), slice(1, 2)),
    (slice(0, 0.5), slice(0, 1)),
    (slice(0.5, 1.5), slice(1, 2)),
]:

    result = s.loc[idx]
    self.check(result, s, res, False)

    # positional indexing
    msg = (
        "cannot do slice indexing "
        rf"on {type(index).__name__} with these indexers \[0\.5\] of "
        "type float"
    )
    with pytest.raises(TypeError, match=msg):
        s[idx]
