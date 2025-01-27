# Extracted from ./data/repos/pandas/pandas/tests/indexing/interval/test_interval_new.py

# loc with slices:
#   - Interval objects: only works with exact matches
#   - scalars: only works for non-overlapping, monotonic intervals,
#     and start/stop select location based on the interval that
#     contains them:
#    (slice_loc(start, stop) == (idx.get_loc(start), idx.get_loc(stop))

ser = series_with_interval_index.copy()

# slice of interval

expected = ser.iloc[:3]
result = indexer_sl(ser)[Interval(0, 1) : Interval(2, 3)]
tm.assert_series_equal(expected, result)

expected = ser.iloc[3:]
result = indexer_sl(ser)[Interval(3, 4) :]
tm.assert_series_equal(expected, result)

msg = "Interval objects are not currently supported"
with pytest.raises(NotImplementedError, match=msg):
    indexer_sl(ser)[Interval(3, 6) :]

with pytest.raises(NotImplementedError, match=msg):
    indexer_sl(ser)[Interval(3, 4, closed="left") :]
