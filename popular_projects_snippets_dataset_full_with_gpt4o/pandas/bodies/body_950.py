# Extracted from ./data/repos/pandas/pandas/tests/indexing/interval/test_interval_new.py

idx = IntervalIndex.from_tuples([(1, 5), (3, 7)])
ser = Series(range(len(idx)), index=idx)

# scalar
expected = ser
result = indexer_sl(ser)[4]
tm.assert_series_equal(expected, result)

result = indexer_sl(ser)[[4]]
tm.assert_series_equal(expected, result)

# interval
expected = 0
result = indexer_sl(ser)[Interval(1, 5)]
result == expected

expected = ser
result = indexer_sl(ser)[[Interval(1, 5), Interval(3, 7)]]
tm.assert_series_equal(expected, result)

with pytest.raises(KeyError, match=re.escape("Interval(3, 5, closed='right')")):
    indexer_sl(ser)[Interval(3, 5)]

msg = r"None of \[\[Interval\(3, 5, closed='right'\)\]\]"
with pytest.raises(KeyError, match=msg):
    indexer_sl(ser)[[Interval(3, 5)]]

# slices with interval (only exact matches)
expected = ser
result = indexer_sl(ser)[Interval(1, 5) : Interval(3, 7)]
tm.assert_series_equal(expected, result)

msg = (
    "'can only get slices from an IntervalIndex if bounds are "
    "non-overlapping and all monotonic increasing or decreasing'"
)
with pytest.raises(KeyError, match=msg):
    indexer_sl(ser)[Interval(1, 6) : Interval(3, 8)]

if indexer_sl is tm.loc:
    # slices with scalar raise for overlapping intervals
    # TODO KeyError is the appropriate error?
    with pytest.raises(KeyError, match=msg):
        ser.loc[1:4]
