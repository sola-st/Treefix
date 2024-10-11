# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py

# GH#2684 (int64)
index = MultiIndex.from_arrays([np.arange(4000)] * 3)
df = DataFrame(np.random.randn(4000).astype("int64"), index=index)

# it works!
result = df.sort_index(level=0)
assert result.index._lexsort_depth == 3

# GH#2684 (int32)
index = MultiIndex.from_arrays([np.arange(4000)] * 3)
df = DataFrame(np.random.randn(4000).astype("int32"), index=index)

# it works!
result = df.sort_index(level=0)
assert (result.dtypes.values == df.dtypes.values).all()
assert result.index._lexsort_depth == 3
