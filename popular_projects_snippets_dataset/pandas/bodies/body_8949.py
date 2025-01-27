# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_accessor.py
# https://github.com/pandas-dev/pandas/issues/30758
df = pd.DataFrame({"sparse": pd.arrays.SparseArray([1, 2])})
assert isinstance(df.sparse, pd.core.arrays.sparse.accessor.SparseFrameAccessor)
