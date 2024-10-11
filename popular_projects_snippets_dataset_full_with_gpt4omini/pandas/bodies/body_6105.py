# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dim2.py
arr2d = data.repeat(2).reshape(-1, 2)
shape = arr2d.shape
assert shape[0] != shape[-1]  # otherwise the rest of the test is useless

assert arr2d.T.shape == shape[::-1]
