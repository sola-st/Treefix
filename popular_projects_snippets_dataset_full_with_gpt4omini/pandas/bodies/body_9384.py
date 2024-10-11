# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_construction.py
# if values has dtype -> respect it
result = constructor(np.array([1, 2], dtype="int8"))
assert result.dtype == Int8Dtype()
result = constructor(np.array([1, 2], dtype="int32"))
assert result.dtype == Int32Dtype()

# if values have no dtype -> always int64
result = constructor([1, 2])
assert result.dtype == Int64Dtype()
