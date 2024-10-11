# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# boolean indexing
d = datetime_frame.index[10]
indexer = datetime_frame.index > d
indexer_obj = indexer.astype(object)

subindex = datetime_frame.index[indexer]
subframe = datetime_frame[indexer]

tm.assert_index_equal(subindex, subframe.index)
with pytest.raises(ValueError, match="Item wrong length"):
    datetime_frame[indexer[:-1]]

subframe_obj = datetime_frame[indexer_obj]
tm.assert_frame_equal(subframe_obj, subframe)

with pytest.raises(ValueError, match="Boolean array expected"):
    datetime_frame[datetime_frame]

# test that Series work
indexer_obj = Series(indexer_obj, datetime_frame.index)

subframe_obj = datetime_frame[indexer_obj]
tm.assert_frame_equal(subframe_obj, subframe)

# test that Series indexers reindex
# we are producing a warning that since the passed boolean
# key is not the same as the given index, we will reindex
# not sure this is really necessary
with tm.assert_produces_warning(UserWarning):
    indexer_obj = indexer_obj.reindex(datetime_frame.index[::-1])
    subframe_obj = datetime_frame[indexer_obj]
    tm.assert_frame_equal(subframe_obj, subframe)

# test df[df > 0]
for df in [
    datetime_frame,
    mixed_float_frame,
    mixed_int_frame,
]:

    data = df._get_numeric_data()
    bif = df[df > 0]
    bifw = DataFrame(
        {c: np.where(data[c] > 0, data[c], np.nan) for c in data.columns},
        index=data.index,
        columns=data.columns,
    )

    # add back other columns to compare
    for c in df.columns:
        if c not in bifw:
            bifw[c] = df[c]
    bifw = bifw.reindex(columns=df.columns)

    tm.assert_frame_equal(bif, bifw, check_dtype=False)
    for c in df.columns:
        if bif[c].dtype != bifw[c].dtype:
            assert bif[c].dtype == df[c].dtype
