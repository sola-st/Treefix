# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_equals.py
# GH#13107
idx = DatetimeIndex(["2011-01-01", "2011-01-02", "NaT"])
assert idx.equals(idx)
assert idx.equals(idx.copy())
assert idx.equals(idx.astype(object))
assert idx.astype(object).equals(idx)
assert idx.astype(object).equals(idx.astype(object))
assert not idx.equals(list(idx))
assert not idx.equals(pd.Series(idx))

idx2 = DatetimeIndex(["2011-01-01", "2011-01-02", "NaT"], tz="US/Pacific")
assert not idx.equals(idx2)
assert not idx.equals(idx2.copy())
assert not idx.equals(idx2.astype(object))
assert not idx.astype(object).equals(idx2)
assert not idx.equals(list(idx2))
assert not idx.equals(pd.Series(idx2))

# same internal, different tz
idx3 = DatetimeIndex(idx.asi8, tz="US/Pacific")
tm.assert_numpy_array_equal(idx.asi8, idx3.asi8)
assert not idx.equals(idx3)
assert not idx.equals(idx3.copy())
assert not idx.equals(idx3.astype(object))
assert not idx.astype(object).equals(idx3)
assert not idx.equals(list(idx3))
assert not idx.equals(pd.Series(idx3))

# check that we do not raise when comparing with OutOfBounds objects
oob = Index([datetime(2500, 1, 1)] * 3, dtype=object)
assert not idx.equals(oob)
assert not idx2.equals(oob)
assert not idx3.equals(oob)

# check that we do not raise when comparing with OutOfBounds dt64
oob2 = oob.map(np.datetime64)
assert not idx.equals(oob2)
assert not idx2.equals(oob2)
assert not idx3.equals(oob2)
