# Extracted from ./data/repos/pandas/pandas/tests/extension/base/constructors.py
if from_series:
    data = pd.Series(data)
result = pd.DataFrame({"A": data})
assert result.dtypes["A"] == data.dtype
assert result.shape == (len(data), 1)
if hasattr(result._mgr, "blocks"):
    assert isinstance(result._mgr.blocks[0], EABackedBlock)
assert isinstance(result._mgr.arrays[0], ExtensionArray)
