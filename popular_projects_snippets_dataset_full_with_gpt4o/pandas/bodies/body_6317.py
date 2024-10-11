# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dtype.py
dtype = data.dtype

# check equivalency for using .dtypes
df = pd.DataFrame(
    {"A": pd.Series(data, dtype=dtype), "B": data, "C": "foo", "D": 1}
)
result = df.dtypes == str(dtype)

try:
    new_numpy_behavior = np.dtype("int64") != "Int64"
except TypeError:
    # numpy<=1.20.3 this comparison could raise or in some cases
    #  come back True
    new_numpy_behavior = True
assert new_numpy_behavior

expected = pd.Series([True, True, False, False], index=list("ABCD"))

self.assert_series_equal(result, expected)

expected = pd.Series([True, True, False, False], index=list("ABCD"))
result = df.dtypes.apply(str) == str(dtype)
self.assert_series_equal(result, expected)
