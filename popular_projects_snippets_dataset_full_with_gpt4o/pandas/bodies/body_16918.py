# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_dataframe.py
# based on asv ConcatDataFrames
df = DataFrame(np.zeros((10000, 200), dtype=np.float32, order=order))

res = concat([df] * 5, axis=axis, ignore_index=ignore_index, copy=True)

for arr in res._iter_column_arrays():
    for arr2 in df._iter_column_arrays():
        assert not np.shares_memory(arr, arr2)
