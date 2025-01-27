# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/manip_ops_test.py
# The axis should be a scalar or 1-D, checked in kernel.
tensor = [[1, 2], [3, 4]]
shift = 1
axis = array_ops.placeholder(dtype=dtypes.int32)
with self.cached_session():
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "axis must be a scalar or a 1-D vector"):
        manip_ops.roll(tensor, shift, axis).eval(feed_dict={axis: [[0, 1]]})
