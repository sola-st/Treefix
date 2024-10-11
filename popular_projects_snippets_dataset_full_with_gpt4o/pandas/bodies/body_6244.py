# Extracted from ./data/repos/pandas/pandas/tests/extension/base/interface.py
# view with no dtype should return a shallow copy, *not* the same
#  object
assert data[1] != data[0]

result = data.view()
assert result is not data
assert type(result) == type(data)

result[1] = result[0]
assert data[1] == data[0]

# check specifically that the `dtype` kwarg is accepted
data.view(dtype=None)
