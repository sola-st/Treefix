# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/manip_ops_test.py
# The shift and axis must be same size, checked in kernel.
tensor = [[1, 2], [3, 4]]
shift = array_ops.placeholder(dtype=dtypes.int32)
axis = [0, 1]
with self.cached_session():
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "shift and axis must have the same size"):
        manip_ops.roll(tensor, shift, axis).eval(feed_dict={shift: [1]})
