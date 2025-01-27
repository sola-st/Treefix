# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softmax_op_test.py
# Test case for GitHub issue 22793.
with self.cached_session():
    ones = array_ops.ones(shape=[2, 3])
    with self.assertRaises(errors_impl.InvalidArgumentError):
        nn_ops.softmax(ones, axis=2).eval()
