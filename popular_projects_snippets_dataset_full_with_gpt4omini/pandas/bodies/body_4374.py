# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
if typ == "int":
    dtypes = MIXED_INT_DTYPES
    arrays = [np.array(np.random.rand(10), dtype=d) for d in dtypes]
elif typ == "float":
    dtypes = MIXED_FLOAT_DTYPES
    arrays = [np.array(np.random.randint(10, size=10), dtype=d) for d in dtypes]

for d, a in zip(dtypes, arrays):
    assert a.dtype == d
ad.update(dict(zip(dtypes, arrays)))
df = DataFrame(ad)

dtypes = MIXED_FLOAT_DTYPES + MIXED_INT_DTYPES
for d in dtypes:
    if d in df:
        assert df.dtypes[d] == d
