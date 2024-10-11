# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# GH13324
# make sure that we are handing non-hashables
arr = np.array([[10.0, 2], 1.0, "apple"], dtype=object)
result, _ = lib.maybe_convert_numeric(arr, set(), False, True)
tm.assert_numpy_array_equal(result, np.array([np.nan, 1.0, np.nan]))
