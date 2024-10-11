# Extracted from ./data/repos/pandas/pandas/tests/extension/base/casting.py
# ensure that astype returns the original object for equal dtype and copy=False
# https://github.com/pandas-dev/pandas/issues/28488
result = data.astype(data.dtype, copy=copy)
assert (result is data) is (not copy)
self.assert_extension_array_equal(result, data)
