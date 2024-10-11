# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_function.py
arr = pd.array(values, dtype="Int64")
result = np.sum(arr)
assert result == expected
