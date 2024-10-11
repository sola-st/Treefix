# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
datetime_series = tm.makeTimeSeries(nper=30)

newFrame = float_frame.reindex(datetime_series.index)

for col in newFrame.columns:
    for idx, val in newFrame[col].items():
        if idx in float_frame.index:
            if np.isnan(val):
                assert np.isnan(float_frame[col][idx])
            else:
                assert val == float_frame[col][idx]
        else:
            assert np.isnan(val)

for col, series in newFrame.items():
    assert tm.equalContents(series.index, newFrame.index)
emptyFrame = float_frame.reindex(Index([]))
assert len(emptyFrame.index) == 0

# Cython code should be unit-tested directly
nonContigFrame = float_frame.reindex(datetime_series.index[::2])

for col in nonContigFrame.columns:
    for idx, val in nonContigFrame[col].items():
        if idx in float_frame.index:
            if np.isnan(val):
                assert np.isnan(float_frame[col][idx])
            else:
                assert val == float_frame[col][idx]
        else:
            assert np.isnan(val)

for col, series in nonContigFrame.items():
    assert tm.equalContents(series.index, nonContigFrame.index)

# corner cases

# Same index, copies values but not index if copy=False
newFrame = float_frame.reindex(float_frame.index, copy=False)
assert newFrame.index is float_frame.index

# length zero
newFrame = float_frame.reindex([])
assert newFrame.empty
assert len(newFrame.columns) == len(float_frame.columns)

# length zero with columns reindexed with non-empty index
newFrame = float_frame.reindex([])
newFrame = newFrame.reindex(float_frame.index)
assert len(newFrame.index) == len(float_frame.index)
assert len(newFrame.columns) == len(float_frame.columns)

# pass non-Index
newFrame = float_frame.reindex(list(datetime_series.index))
expected = datetime_series.index._with_freq(None)
tm.assert_index_equal(newFrame.index, expected)

# copy with no axes
result = float_frame.reindex()
tm.assert_frame_equal(result, float_frame)
assert result is not float_frame
