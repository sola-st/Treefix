# Extracted from ./data/repos/pandas/pandas/tests/extension/base/constructors.py
result = pd.Series(data)
assert result.dtype == data.dtype
assert len(result) == len(data)
if hasattr(result._mgr, "blocks"):
    assert isinstance(result._mgr.blocks[0], EABackedBlock)
assert result._mgr.array is data

# Series[EA] is unboxed / boxed correctly
result2 = pd.Series(result)
assert result2.dtype == data.dtype
if hasattr(result._mgr, "blocks"):
    assert isinstance(result2._mgr.blocks[0], EABackedBlock)
