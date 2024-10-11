# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/core/custom_float_test.py
values_to_sort = np.float32(
    float_type(np.float32(FLOAT_VALUES[float_type])))
argmax_f32 = np.argmax(values_to_sort)
argmax_float_type = np.argmax(values_to_sort.astype(float_type))  # pylint: disable=too-many-function-args
np.testing.assert_equal(argmax_f32, argmax_float_type)
