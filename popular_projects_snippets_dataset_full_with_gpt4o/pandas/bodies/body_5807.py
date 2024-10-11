# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
# GH 42600
expected = pd.Series(data)
expected_sliced = expected.head(2)
full_pickled = pickle.dumps(expected)
sliced_pickled = pickle.dumps(expected_sliced)

assert len(full_pickled) > len(sliced_pickled)

result = pickle.loads(full_pickled)
tm.assert_series_equal(result, expected)

result_sliced = pickle.loads(sliced_pickled)
tm.assert_series_equal(result_sliced, expected_sliced)
