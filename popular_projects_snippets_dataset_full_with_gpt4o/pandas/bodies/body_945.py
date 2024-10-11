# Extracted from ./data/repos/pandas/pandas/tests/indexing/interval/test_interval_new.py

# loc with single label / list of labels:
#   - Intervals: only exact matches
#   - scalars: those that contain it

ser = series_with_interval_index.copy()

assert indexer_sl(ser)[1] == 0
assert indexer_sl(ser)[1.5] == 1
assert indexer_sl(ser)[2] == 1

expected = ser.iloc[1:4]
tm.assert_series_equal(expected, indexer_sl(ser)[[1.5, 2.5, 3.5]])
tm.assert_series_equal(expected, indexer_sl(ser)[[2, 3, 4]])
tm.assert_series_equal(expected, indexer_sl(ser)[[1.5, 3, 4]])

expected = ser.iloc[[1, 1, 2, 1]]
tm.assert_series_equal(expected, indexer_sl(ser)[[1.5, 2, 2.5, 1.5]])

expected = ser.iloc[2:5]
tm.assert_series_equal(expected, indexer_sl(ser)[ser >= 2])
