# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
# append to existing multiindex
df = frame_of_index_cols.set_index(["D"], drop=drop, append=True)

keys = keys if isinstance(keys, list) else [keys]
expected = frame_of_index_cols.set_index(["D"] + keys, drop=drop, append=True)

result = df.set_index(keys, drop=drop, append=True)

tm.assert_frame_equal(result, expected)
