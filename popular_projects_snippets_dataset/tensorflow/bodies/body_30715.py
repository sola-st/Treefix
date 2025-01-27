# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/manip_ops_test.py
# The shift should be a scalar or 1-D, checked in kernel.
tensor = [[1, 2], [3, 4]]
shift = array_ops.placeholder(dtype=dtypes.int32)
axis = 1
with self.cached_session():
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "shift must be a scalar or a 1-D vector"):
        manip_ops.roll(tensor, shift, axis).eval(feed_dict={shift: [[0, 1]]})
