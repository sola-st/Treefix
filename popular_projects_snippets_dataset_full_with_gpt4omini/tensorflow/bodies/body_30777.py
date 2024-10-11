# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/bitcast_op_test.py
x = np.zeros([1, 1], np.int8)
datatype = dtypes.int32
# When eager_op_as_function is enabled shape inference will raise
# a different more informative error message.
with self.assertRaisesRegex(
    (ValueError, errors.InvalidArgumentError),
    "Cannot bitcast from 6 to 3|convert from s8.* to S32"):
    array_ops.bitcast(x, datatype, None)
