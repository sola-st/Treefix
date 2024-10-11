# Extracted from ./data/repos/pandas/pandas/tests/extension/base/reshaping.py
result = data.transpose()
assert type(result) == type(data)

# check we get a new object
assert result is not data

# If we ever _did_ support 2D, shape should be reversed
assert result.shape == data.shape[::-1]

# Check that we have a view, not a copy
result[0] = result[1]
assert data[0] == data[1]
