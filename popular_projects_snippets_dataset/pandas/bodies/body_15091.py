# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
obj = pd.Index(arr, copy=False)
if as_series:
    obj = Series(obj.values, copy=False)

# no copy by default
result = obj.to_numpy()
assert np.shares_memory(arr, result) is True

result = obj.to_numpy(copy=False)
assert np.shares_memory(arr, result) is True

# copy=True
result = obj.to_numpy(copy=True)
assert np.shares_memory(arr, result) is False
