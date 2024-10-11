# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
values_to_sort = np.float32(
    float_type(np.float32(FLOAT_VALUES[float_type])))
argmin_f32 = np.argmin(values_to_sort)
argmin_float_type = np.argmin(values_to_sort.astype(float_type))  # pylint: disable=too-many-function-args
np.testing.assert_equal(argmin_f32, argmin_float_type)
