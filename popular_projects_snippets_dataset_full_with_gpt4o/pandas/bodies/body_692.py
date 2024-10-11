# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# infer_dtype `skipna` default deprecated in GH#24050,
#  changed to True in GH#29876
arr = np.array([1, 2, 3, np.nan], dtype=object)

result = lib.infer_dtype(arr)
assert result == "integer"
