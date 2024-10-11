# Extracted from ./data/repos/pandas/pandas/tests/extension/base/interface.py
assert is_extension_array_dtype(data)
assert is_extension_array_dtype(data.dtype)
assert is_extension_array_dtype(pd.Series(data))
assert isinstance(data.dtype, ExtensionDtype)
