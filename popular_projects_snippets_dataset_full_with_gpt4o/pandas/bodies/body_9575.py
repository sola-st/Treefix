# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_construction.py
# if values has dtype -> respect it
result = pd.array(np.array([1, 2], dtype="float32"))
assert result.dtype == Float32Dtype()

# if values have no dtype -> always float64
result = pd.array([1.0, 2.0])
assert result.dtype == Float64Dtype()
