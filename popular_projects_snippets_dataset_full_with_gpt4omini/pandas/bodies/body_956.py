# Extracted from ./data/repos/pandas/pandas/tests/indexing/interval/test_interval.py

ser = series_with_interval_index.copy()

expected = ser.iloc[:3]
tm.assert_series_equal(expected, indexer_sl(ser)[:3])
tm.assert_series_equal(expected, indexer_sl(ser)[:2.5])
tm.assert_series_equal(expected, indexer_sl(ser)[0.1:2.5])
if indexer_sl is tm.loc:
    tm.assert_series_equal(expected, ser.loc[-1:3])

expected = ser.iloc[1:4]
tm.assert_series_equal(expected, indexer_sl(ser)[[1.5, 2.5, 3.5]])
tm.assert_series_equal(expected, indexer_sl(ser)[[2, 3, 4]])
tm.assert_series_equal(expected, indexer_sl(ser)[[1.5, 3, 4]])

expected = ser.iloc[2:5]
tm.assert_series_equal(expected, indexer_sl(ser)[ser >= 2])
