# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
index_cls = self._index_cls

# explicit construction
index = index_cls([1, 2, 3, 4, 5], dtype=dtype)

assert isinstance(index, index_cls)
assert index.dtype == dtype

expected = np.array([1, 2, 3, 4, 5], dtype=dtype)
tm.assert_numpy_array_equal(index.values, expected)

index = index_cls(np.array([1, 2, 3, 4, 5]), dtype=dtype)
assert isinstance(index, index_cls)
assert index.dtype == dtype

index = index_cls([1.0, 2, 3, 4, 5], dtype=dtype)
assert isinstance(index, index_cls)
assert index.dtype == dtype

index = index_cls(np.array([1.0, 2, 3, 4, 5]), dtype=dtype)
assert isinstance(index, index_cls)
assert index.dtype == dtype

index = index_cls([1.0, 2, 3, 4, 5], dtype=dtype)
assert isinstance(index, index_cls)
assert index.dtype == dtype

index = index_cls(np.array([1.0, 2, 3, 4, 5]), dtype=dtype)
assert isinstance(index, index_cls)
assert index.dtype == dtype

# nan handling
result = index_cls([np.nan, np.nan], dtype=dtype)
assert pd.isna(result.values).all()

result = index_cls(np.array([np.nan]), dtype=dtype)
assert pd.isna(result.values).all()
