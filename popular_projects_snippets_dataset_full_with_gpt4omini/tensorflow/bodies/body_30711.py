# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/manip_ops_test.py
# The input should be 1-D or higher, checked in kernel.
tensor = array_ops.placeholder(dtype=dtypes.int32)
shift = 1
axis = 0
with self.cached_session():
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "input must be 1-D or higher"):
        manip_ops.roll(tensor, shift, axis).eval(feed_dict={tensor: 7})
