# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
arr = ["a", np.nan, "c"]
result = lib.infer_dtype(arr, skipna=False)
# This currently returns "mixed", but it's not clear that's optimal.
# This could also return "string" or "mixed-string"
assert result == "mixed"

# even though we use skipna, we are only skipping those NAs that are
#  considered matching by is_string_array
arr = ["a", np.nan, "c"]
result = lib.infer_dtype(arr, skipna=True)
assert result == "string"

arr = ["a", pd.NA, "c"]
result = lib.infer_dtype(arr, skipna=True)
assert result == "string"

arr = ["a", pd.NaT, "c"]
result = lib.infer_dtype(arr, skipna=True)
assert result == "mixed"

arr = ["a", "c"]
result = lib.infer_dtype(arr, skipna=False)
assert result == "string"
