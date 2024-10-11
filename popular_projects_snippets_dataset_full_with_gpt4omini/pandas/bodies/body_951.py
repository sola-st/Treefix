# Extracted from ./data/repos/pandas/pandas/tests/indexing/interval/test_interval_new.py

idx = IntervalIndex.from_tuples([(1, 3), (3, 7)])
ser = Series(range(len(idx)), index=idx)

result = indexer_sl(ser)[Interval(1, 3)]
assert result == 0

result = indexer_sl(ser)[[Interval(1, 3)]]
expected = ser.iloc[0:1]
tm.assert_series_equal(expected, result)
