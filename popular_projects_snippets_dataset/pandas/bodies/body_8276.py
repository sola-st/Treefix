# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_astype.py
converted = rng.to_pydatetime()
assert isinstance(converted, np.ndarray)
for x, stamp in zip(converted, rng):
    assert isinstance(x, datetime)
    assert x == stamp.to_pydatetime()
    assert x.tzinfo == stamp.tzinfo
