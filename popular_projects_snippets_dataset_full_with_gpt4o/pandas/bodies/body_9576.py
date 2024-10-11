# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_construction.py
result = pd.array([1, 2], dtype="Float32")
assert result.dtype == Float32Dtype()

# if values has dtype -> override it
result = pd.array(np.array([1, 2], dtype="float32"), dtype="Float64")
assert result.dtype == Float64Dtype()
