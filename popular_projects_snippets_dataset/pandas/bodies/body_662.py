# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# See PR 12215
arr = np.array(["42E", "2E", "99e", "6e"], dtype="O")
result, _ = lib.maybe_convert_numeric(arr, set(), False, True)
assert np.all(np.isnan(result))
