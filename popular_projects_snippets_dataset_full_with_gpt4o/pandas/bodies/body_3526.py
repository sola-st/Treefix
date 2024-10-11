# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
df = frame_of_index_cols

if isinstance(keys, list):
    idx = MultiIndex.from_arrays([df[x] for x in keys], names=keys)
else:
    idx = Index(df[keys], name=keys)
expected = df.drop(keys, axis=1) if drop else df
expected.index = idx

if inplace:
    result = df.copy()
    return_value = result.set_index(keys, drop=drop, inplace=True)
    assert return_value is None
else:
    result = df.set_index(keys, drop=drop)

tm.assert_frame_equal(result, expected)
