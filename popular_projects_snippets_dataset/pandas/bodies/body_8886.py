# Extracted from ./data/repos/pandas/pandas/tests/arrays/interval/test_interval.py
# GH27219
tuples = [(left, left), (left, right), np.nan]
expected = np.array([closed != "both", False, False])
result = constructor.from_tuples(tuples, closed=closed).is_empty
tm.assert_numpy_array_equal(result, expected)
