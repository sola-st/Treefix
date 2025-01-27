# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_function.py
arr = pd.array(values, dtype="Float64")
result = np.sum(arr)
assert result == expected
