# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
# GH 16877

if idx_dtype == "range":
    numeric_index = RangeIndex(4)
else:
    numeric_index = Index(np.arange(4, dtype=idx_dtype))

other = Index([True, False, True])

result = getattr(numeric_index, method)(other)
expected = np.array([-1, -1, -1], dtype=np.intp)
if method == "get_indexer":
    tm.assert_numpy_array_equal(result, expected)
else:
    missing = np.arange(3, dtype=np.intp)
    tm.assert_numpy_array_equal(result[0], expected)
    tm.assert_numpy_array_equal(result[1], missing)
