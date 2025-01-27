# Extracted from ./data/repos/pandas/pandas/tests/extension/base/constructors.py
cls = dtype.construct_array_type()
result = cls._empty((4,), dtype=dtype)
assert isinstance(result, cls)
assert result.dtype == dtype
assert result.shape == (4,)

# GH#19600 method on ExtensionDtype
result2 = dtype.empty((4,))
assert isinstance(result2, cls)
assert result2.dtype == dtype
assert result2.shape == (4,)

result2 = dtype.empty(4)
assert isinstance(result2, cls)
assert result2.dtype == dtype
assert result2.shape == (4,)
