# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_index.py
frame = multiindex_dataframe_random_data
index = frame.index
result = concat([frame, frame], keys=[0, 1], names=["iteration"])

assert result.index.names == ("iteration",) + index.names
tm.assert_frame_equal(result.loc[0], frame)
tm.assert_frame_equal(result.loc[1], frame)
assert result.index.nlevels == 3
