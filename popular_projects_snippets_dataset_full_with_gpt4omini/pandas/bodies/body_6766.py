# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# GH 20636
breaks = np.arange(5, dtype=any_real_numpy_dtype)
index = IntervalIndex.from_breaks(breaks)
key = make_key(breaks)

# test if _maybe_convert_i8 won't change key if an Interval or IntervalIndex
result = index._maybe_convert_i8(key)
assert result is key
