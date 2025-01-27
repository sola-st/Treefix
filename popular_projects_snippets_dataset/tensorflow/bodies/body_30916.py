# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softmax_op_test.py
with self.cached_session():
    # Use placeholder to make sure we get runtime error instead of shape
    # inference error.
    dim = array_ops.placeholder_with_default(100, shape=[])
    with self.assertRaises(errors_impl.InvalidArgumentError):
        nn_ops.softmax([1., 2., 3., 4.], axis=dim).eval()
