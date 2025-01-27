# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py

# floats are not ok
# strip Index to convert PeriodIndex -> Period
# We don't care whether the error message says
# PeriodIndex or PeriodArray
msg = f"Cannot cast {type(index).__name__.rstrip('Index')}.*? to "

with pytest.raises(TypeError, match=msg):
    Series(index, dtype=float)

# ints are ok
# we test with np.int64 to get similar results on
# windows / 32-bit platforms
result = Series(index, dtype=np.int64)
expected = Series(index.astype(np.int64))
tm.assert_series_equal(result, expected)
