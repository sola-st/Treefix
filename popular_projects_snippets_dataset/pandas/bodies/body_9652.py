# Extracted from ./data/repos/pandas/pandas/tests/arrays/masked_shared.py

# array
result = pd.Series(op(data, other))
expected = pd.Series(op(data._data, other), dtype="boolean")

# fill the nan locations
expected[data._mask] = pd.NA

tm.assert_series_equal(result, expected)

# series
ser = pd.Series(data)
result = op(ser, other)

expected = op(pd.Series(data._data), other)

# fill the nan locations
expected[data._mask] = pd.NA
expected = expected.astype("boolean")

tm.assert_series_equal(result, expected)
