# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
frame = multiindex_dataframe_random_data
subset = frame.index[[1, 4, 5]]

frame.loc[subset] = 99
assert (frame.loc[subset].values == 99).all()

frame_original = frame.copy()
col = frame["B"]
col[subset] = 97
if using_copy_on_write:
    # chained setitem doesn't work with CoW
    tm.assert_frame_equal(frame, frame_original)
else:
    assert (frame.loc[subset, "B"] == 97).all()
