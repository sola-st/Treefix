# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
# Have to override to specify that fill_value will change.
fill_value = data_missing[1]

result = pd.DataFrame({"A": data_missing, "B": [1, 2]}).fillna(fill_value)

if pd.isna(data_missing.fill_value):
    dtype = SparseDtype(data_missing.dtype, fill_value)
else:
    dtype = data_missing.dtype

expected = pd.DataFrame(
    {
        "A": data_missing._from_sequence([fill_value, fill_value], dtype=dtype),
        "B": [1, 2],
    }
)

self.assert_frame_equal(result, expected)
