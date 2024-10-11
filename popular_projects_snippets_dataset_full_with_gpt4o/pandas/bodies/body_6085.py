# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
result = data[idx]
assert len(result) == 3
assert isinstance(result, type(data))
expected = data.take([0, 1, 2])
self.assert_extension_array_equal(result, expected)

expected = pd.Series(expected)
result = pd.Series(data)[idx]
self.assert_series_equal(result, expected)
