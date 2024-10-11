# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
# Indexing with empty list
result = data[[]]
assert len(result) == 0
assert isinstance(result, type(data))

expected = data[np.array([], dtype="int64")]
self.assert_extension_array_equal(result, expected)
