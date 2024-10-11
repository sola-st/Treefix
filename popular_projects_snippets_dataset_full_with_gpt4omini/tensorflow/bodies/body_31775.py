# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/nth_element_op_test.py
inputs = [[0.1, 0.2], [0.3, 0.4]]
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "must have last dimension > n = 2"):
    nn_ops.nth_element(inputs, 2)

# Test with placeholders
with ops.Graph().as_default():
    with self.session(use_gpu=False):
        n = array_ops.placeholder(dtypes.int32)
        values = nn_ops.nth_element(inputs, n)
        with self.assertRaisesOpError("must have last dimension > n = 2"):
            values.eval(feed_dict={n: 2})
