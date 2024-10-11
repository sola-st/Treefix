# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
# GH49795
pd_array = data._data.to_pandas().array
result = pd_array.astype(data.dtype)
assert not isinstance(pd_array.dtype, ArrowDtype)
assert isinstance(result.dtype, ArrowDtype)
tm.assert_extension_array_equal(result, data)
