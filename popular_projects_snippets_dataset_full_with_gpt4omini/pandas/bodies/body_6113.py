# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dim2.py
arr2d = data.reshape(1, -1)

objs = list(iter(arr2d))
assert len(objs) == arr2d.shape[0]

for obj in objs:
    assert isinstance(obj, type(data))
    assert obj.dtype == data.dtype
    assert obj.ndim == 1
    assert len(obj) == arr2d.shape[1]
