# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_floats.py

# related 236
# scalar/slicing of a float index
s = Series(np.arange(5), index=np.arange(5) * 2.5, dtype=np.int64)

# label based slicing
result = indexer_sl(s)[1.0:3.0]
expected = Series(1, index=[2.5])
tm.assert_series_equal(result, expected)

# exact indexing when found

result = indexer_sl(s)[5.0]
assert result == 2

result = indexer_sl(s)[5]
assert result == 2

# value not found (and no fallbacking at all)

# scalar integers
with pytest.raises(KeyError, match=r"^4$"):
    indexer_sl(s)[4]

# fancy floats/integers create the correct entry (as nan)
# fancy tests
expected = Series([2, 0], index=Index([5.0, 0.0], dtype=np.float64))
for fancy_idx in [[5.0, 0.0], np.array([5.0, 0.0])]:  # float
    tm.assert_series_equal(indexer_sl(s)[fancy_idx], expected)

expected = Series([2, 0], index=Index([5, 0], dtype="float64"))
for fancy_idx in [[5, 0], np.array([5, 0])]:
    tm.assert_series_equal(indexer_sl(s)[fancy_idx], expected)

# all should return the same as we are slicing 'the same'
result1 = indexer_sl(s)[2:5]
result2 = indexer_sl(s)[2.0:5.0]
result3 = indexer_sl(s)[2.0:5]
result4 = indexer_sl(s)[2.1:5]
tm.assert_series_equal(result1, result2)
tm.assert_series_equal(result1, result3)
tm.assert_series_equal(result1, result4)

expected = Series([1, 2], index=[2.5, 5.0])
result = indexer_sl(s)[2:5]

tm.assert_series_equal(result, expected)

# list selection
result1 = indexer_sl(s)[[0.0, 5, 10]]
result2 = s.iloc[[0, 2, 4]]
tm.assert_series_equal(result1, result2)

with pytest.raises(KeyError, match="not in index"):
    indexer_sl(s)[[1.6, 5, 10]]

with pytest.raises(KeyError, match="not in index"):
    indexer_sl(s)[[0, 1, 2]]

result = indexer_sl(s)[[2.5, 5]]
tm.assert_series_equal(result, Series([1, 2], index=[2.5, 5.0]))

result = indexer_sl(s)[[2.5]]
tm.assert_series_equal(result, Series([1], index=[2.5]))
