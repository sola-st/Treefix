# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
df = frame_of_index_cols

keys = keys if isinstance(keys, list) else [keys]
idx = MultiIndex.from_arrays(
    [df.index] + [df[x] for x in keys], names=[None] + keys
)
expected = df.drop(keys, axis=1) if drop else df.copy()
expected.index = idx

result = df.set_index(keys, drop=drop, append=True)

tm.assert_frame_equal(result, expected)
