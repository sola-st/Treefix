# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
rng = list(range(10))
ser = Series(10, index=rng)
df = DataFrame(rng, index=rng)
msg = (
    "Indexing a Series with DataFrame is not supported, "
    "use the appropriate DataFrame column"
)
with pytest.raises(TypeError, match=msg):
    ser[df > 5]
