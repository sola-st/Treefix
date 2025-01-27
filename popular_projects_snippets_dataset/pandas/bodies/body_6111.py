# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dim2.py
arr2d = data.reshape(-1, 1)
assert arr2d.shape == (data.size, 1)
assert len(arr2d) == len(data)

arr2d = data.reshape((-1, 1))
assert arr2d.shape == (data.size, 1)
assert len(arr2d) == len(data)

with pytest.raises(ValueError):
    data.reshape((data.size, 2))
with pytest.raises(ValueError):
    data.reshape(data.size, 2)
