# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_astype.py
# int64 -> uint64 fails with negative values
index = interval_range(-10, 10)
dtype = IntervalDtype("uint64", "right")

# Until we decide what the exception message _should_ be, we
#  assert something that it should _not_ be.
#  We should _not_ be getting a message suggesting that the -10
#  has been wrapped around to a large-positive integer
msg = "^(?!(left side of interval must be <= right side))"
with pytest.raises(ValueError, match=msg):
    index.astype(dtype)
