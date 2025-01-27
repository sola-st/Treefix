# Extracted from ./data/repos/pandas/pandas/tests/extension/base/reshaping.py
# as long as EA is 1D-only, ravel is a no-op
result = data.ravel()
assert type(result) == type(data)

# Check that we have a view, not a copy
result[0] = result[1]
assert data[0] == data[1]
