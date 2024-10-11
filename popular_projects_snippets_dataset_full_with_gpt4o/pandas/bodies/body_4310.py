# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# TimeSeries
ts = datetime_frame["A"]

# 10890
# we no longer allow auto timeseries broadcasting
# and require explicit broadcasting
added = datetime_frame.add(ts, axis="index")

for key, col in datetime_frame.items():
    result = col + ts
    tm.assert_series_equal(added[key], result, check_names=False)
    assert added[key].name == key
    if col.name == ts.name:
        assert result.name == "A"
    else:
        assert result.name is None

smaller_frame = datetime_frame[:-5]
smaller_added = smaller_frame.add(ts, axis="index")

tm.assert_index_equal(smaller_added.index, datetime_frame.index)

smaller_ts = ts[:-5]
smaller_added2 = datetime_frame.add(smaller_ts, axis="index")
tm.assert_frame_equal(smaller_added, smaller_added2)

# length 0, result is all-nan
result = datetime_frame.add(ts[:0], axis="index")
expected = DataFrame(
    np.nan, index=datetime_frame.index, columns=datetime_frame.columns
)
tm.assert_frame_equal(result, expected)

# Frame is all-nan
result = datetime_frame[:0].add(ts, axis="index")
expected = DataFrame(
    np.nan, index=datetime_frame.index, columns=datetime_frame.columns
)
tm.assert_frame_equal(result, expected)

# empty but with non-empty index
frame = datetime_frame[:1].reindex(columns=[])
result = frame.mul(ts, axis="index")
assert len(result) == len(ts)
