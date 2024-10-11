# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
idx1 = date_range("2015-01-01 10:00", freq="D", periods=3, tz="US/Eastern")
idx2 = date_range("2015-01-01 10:00", freq="H", periods=3)
idx3 = pd.timedelta_range("1 days", freq="D", periods=3)
idx4 = pd.period_range("2011-01-01", freq="D", periods=3)

result = MultiIndex.from_arrays([idx1, idx2, idx3, idx4])
tm.assert_index_equal(result.get_level_values(0), idx1)
tm.assert_index_equal(result.get_level_values(1), idx2)
tm.assert_index_equal(result.get_level_values(2), idx3)
tm.assert_index_equal(result.get_level_values(3), idx4)

result2 = MultiIndex.from_arrays(
    [Series(idx1), Series(idx2), Series(idx3), Series(idx4)]
)
tm.assert_index_equal(result2.get_level_values(0), idx1)
tm.assert_index_equal(result2.get_level_values(1), idx2)
tm.assert_index_equal(result2.get_level_values(2), idx3)
tm.assert_index_equal(result2.get_level_values(3), idx4)

tm.assert_index_equal(result, result2)
