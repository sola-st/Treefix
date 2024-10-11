# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
rng = date_range("1/1/2000", periods=20)

result = rng.get_indexer(rng.map(lambda x: x.date()))
expected = rng.get_indexer(rng)
tm.assert_numpy_array_equal(result, expected)
