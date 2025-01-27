# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_equals.py
# GH#13107
idx = PeriodIndex(["2011-01-01", "2011-01-02", "NaT"], freq=freq)
assert idx.equals(idx)
assert idx.equals(idx.copy())
assert idx.equals(idx.astype(object))
assert idx.astype(object).equals(idx)
assert idx.astype(object).equals(idx.astype(object))
assert not idx.equals(list(idx))
assert not idx.equals(pd.Series(idx))

idx2 = PeriodIndex(["2011-01-01", "2011-01-02", "NaT"], freq="H")
assert not idx.equals(idx2)
assert not idx.equals(idx2.copy())
assert not idx.equals(idx2.astype(object))
assert not idx.astype(object).equals(idx2)
assert not idx.equals(list(idx2))
assert not idx.equals(pd.Series(idx2))

# same internal, different tz
idx3 = PeriodIndex._simple_new(
    idx._values._simple_new(idx._values.asi8, freq="H")
)
tm.assert_numpy_array_equal(idx.asi8, idx3.asi8)
assert not idx.equals(idx3)
assert not idx.equals(idx3.copy())
assert not idx.equals(idx3.astype(object))
assert not idx.astype(object).equals(idx3)
assert not idx.equals(list(idx3))
assert not idx.equals(pd.Series(idx3))
