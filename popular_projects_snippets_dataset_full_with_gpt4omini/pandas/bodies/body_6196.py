# Extracted from ./data/repos/pandas/pandas/tests/extension/base/constructors.py
result = pd.DataFrame(pd.Series(data))
assert result.dtypes[0] == data.dtype
assert result.shape == (len(data), 1)
if hasattr(result._mgr, "blocks"):
    assert isinstance(result._mgr.blocks[0], EABackedBlock)
assert isinstance(result._mgr.arrays[0], ExtensionArray)
