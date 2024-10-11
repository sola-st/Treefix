# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
num_df = DataFrame([[1, 2], [4, 5, 6]])
result = read_json(
    num_df.to_json(orient=orient),
    orient=orient,
    convert_axes=convert_axes,
    dtype=dtype,
)
assert np.isnan(result.iloc[0, 2])

obj_df = DataFrame([["1", "2"], ["4", "5", "6"]])
result = read_json(
    obj_df.to_json(orient=orient),
    orient=orient,
    convert_axes=convert_axes,
    dtype=dtype,
)
assert np.isnan(result.iloc[0, 2])
