# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
# Note: np.sort doesn't work properly with NaNs since they always compare
# False.
values_to_sort = np.float32(
    [x for x in FLOAT_VALUES[float_type] if not np.isnan(x)])
sorted_f32 = np.sort(values_to_sort)
sorted_float_type = np.sort(values_to_sort.astype(float_type))  # pylint: disable=too-many-function-args
np.testing.assert_equal(sorted_f32, np.float32(sorted_float_type))
