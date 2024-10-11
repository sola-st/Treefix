# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# GH 20636
breaks = np.arange(5, dtype=any_real_numpy_dtype)
index = IntervalIndex.from_breaks(breaks)
key = make_key(breaks)

result = index._maybe_convert_i8(key)
kind = breaks.dtype.kind
expected_dtype = {"i": np.int64, "u": np.uint64, "f": np.float64}[kind]
expected = Index(key, dtype=expected_dtype)
tm.assert_index_equal(result, expected)
