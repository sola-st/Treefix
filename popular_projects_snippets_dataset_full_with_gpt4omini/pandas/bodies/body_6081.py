# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
# Empty mask, raw array
mask = np.zeros(len(data), dtype=bool)
result = data[mask]
assert len(result) == 0
assert isinstance(result, type(data))

# Empty mask, in series
mask = np.zeros(len(data), dtype=bool)
result = pd.Series(data)[mask]
assert len(result) == 0
assert result.dtype == data.dtype

# non-empty mask, raw array
mask[0] = True
result = data[mask]
assert len(result) == 1
assert isinstance(result, type(data))

# non-empty mask, in series
result = pd.Series(data)[mask]
assert len(result) == 1
assert result.dtype == data.dtype
