# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_construction.py
result = constructor([1, 2], dtype="Int8")
assert result.dtype == Int8Dtype()

# if values has dtype -> override it
result = constructor(np.array([1, 2], dtype="int8"), dtype="Int32")
assert result.dtype == Int32Dtype()
