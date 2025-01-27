# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_formats.py
# GH 28210
index = IntervalIndex.from_tuples(tuples, closed=closed)
result = index._format_native_types()
expected = np.array(expected_data)
tm.assert_numpy_array_equal(result, expected)
