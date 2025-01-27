# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
obj = series_with_simple_index
key = 0 if (indexer is tm.iloc or len(obj) == 0) else obj.index[0]

if indexer is tm.loc and is_bool_dtype(obj.index):
    # passing [False] will get interpreted as a boolean mask
    # TODO: should it?  unambiguous when lengths dont match?
    exit()
if indexer is tm.loc and isinstance(obj.index, MultiIndex):
    msg = "MultiIndex does not support indexing with Ellipsis"
    with pytest.raises(NotImplementedError, match=msg):
        result = indexer(obj)[..., [key]]

elif len(obj) != 0:
    result = indexer(obj)[..., [key]]
    expected = indexer(obj)[[key]]
    tm.assert_series_equal(result, expected)

key2 = 0 if indexer is tm.iloc else obj.name
df = obj.to_frame()
result = indexer(df)[..., [key2]]
expected = indexer(df)[:, [key2]]
tm.assert_frame_equal(result, expected)
