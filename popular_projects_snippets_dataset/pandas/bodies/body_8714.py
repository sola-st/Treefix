# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
arr = np.array([1, 2, 3], dtype=np.int64)
expected = self.array_cls(arr, dtype=self.example_dtype)

data = pd.array(arr, dtype="Int64")
result = self.array_cls(data, dtype=self.example_dtype)

tm.assert_extension_array_equal(result, expected)
