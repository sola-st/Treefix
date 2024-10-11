# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dim2.py
arr = data_missing.repeat(2).reshape(2, 2)
assert arr[0].isna().all()
assert not arr[1].isna().any()

result = arr.fillna(method=method)

expected = data_missing.fillna(method=method).repeat(2).reshape(2, 2)
self.assert_extension_array_equal(result, expected)
