# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
arr = np.array(["inf", "inf", "inf"], dtype="O")
result, _ = lib.maybe_convert_numeric(arr, set(), False)
assert result.dtype == np.float64

arr = np.array(["-inf", "-inf", "-inf"], dtype="O")
result, _ = lib.maybe_convert_numeric(arr, set(), False)
assert result.dtype == np.float64
