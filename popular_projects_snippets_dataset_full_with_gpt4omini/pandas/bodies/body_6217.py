# Extracted from ./data/repos/pandas/pandas/tests/extension/base/casting.py
ser = pd.Series(all_data, name="A")
result = ser.astype(object)
assert result.dtype == np.dtype(object)
if hasattr(result._mgr, "blocks"):
    assert isinstance(result._mgr.blocks[0], ObjectBlock)
assert isinstance(result._mgr.array, np.ndarray)
assert result._mgr.array.dtype == np.dtype(object)
