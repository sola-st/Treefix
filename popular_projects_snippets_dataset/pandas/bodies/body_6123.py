# Extracted from ./data/repos/pandas/pandas/tests/extension/base/reshaping.py
wrapped = pd.Series(data)
if in_frame:
    wrapped = pd.DataFrame(wrapped)
result = pd.concat([wrapped, wrapped], ignore_index=True)

assert len(result) == len(data) * 2

if in_frame:
    dtype = result.dtypes[0]
else:
    dtype = result.dtype

assert dtype == data.dtype
if hasattr(result._mgr, "blocks"):
    assert isinstance(result._mgr.blocks[0], EABackedBlock)
assert isinstance(result._mgr.arrays[0], ExtensionArray)
