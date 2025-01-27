# Extracted from ./data/repos/pandas/pandas/tests/indexing/interval/test_interval_new.py

idx = IntervalIndex.from_tuples([(1, 3), (1, 3), (3, 7)])
ser = Series(range(len(idx)), index=idx)

expected = ser.iloc[[0, 1]]
result = indexer_sl(ser)[Interval(1, 3)]
tm.assert_series_equal(expected, result)

expected = ser
result = indexer_sl(ser)[Interval(1, 3) :]
tm.assert_series_equal(expected, result)

expected = ser.iloc[[0, 1]]
result = indexer_sl(ser)[[Interval(1, 3)]]
tm.assert_series_equal(expected, result)
