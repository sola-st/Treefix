# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dim2.py
arr2d = data.reshape(1, -1)

result = arr2d.tolist()
expected = [data.tolist()]

assert isinstance(result, list)
assert all(isinstance(x, list) for x in result)

assert result == expected
