# Extracted from ./data/repos/pandas/pandas/tests/indexing/interval/test_interval_new.py

# loc with single label / list of labels:
#   - Intervals: only exact matches
#   - scalars: those that contain it

ser = series_with_interval_index.copy()

expected = 0
result = indexer_sl(ser)[Interval(0, 1)]
assert result == expected

expected = ser.iloc[3:5]
result = indexer_sl(ser)[[Interval(3, 4), Interval(4, 5)]]
tm.assert_series_equal(expected, result)

# missing or not exact
with pytest.raises(KeyError, match=re.escape("Interval(3, 5, closed='left')")):
    indexer_sl(ser)[Interval(3, 5, closed="left")]

with pytest.raises(KeyError, match=re.escape("Interval(3, 5, closed='right')")):
    indexer_sl(ser)[Interval(3, 5)]

with pytest.raises(
    KeyError, match=re.escape("Interval(-2, 0, closed='right')")
):
    indexer_sl(ser)[Interval(-2, 0)]

with pytest.raises(KeyError, match=re.escape("Interval(5, 6, closed='right')")):
    indexer_sl(ser)[Interval(5, 6)]
