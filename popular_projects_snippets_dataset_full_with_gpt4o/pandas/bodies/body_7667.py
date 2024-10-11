# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
result = MultiIndex.from_arrays([idx1, idx2])
tm.assert_index_equal(result.get_level_values(0), idx1)
tm.assert_index_equal(result.get_level_values(1), idx2)

result2 = MultiIndex.from_arrays([Series(idx1), Series(idx2)])
tm.assert_index_equal(result2.get_level_values(0), idx1)
tm.assert_index_equal(result2.get_level_values(1), idx2)

tm.assert_index_equal(result, result2)
