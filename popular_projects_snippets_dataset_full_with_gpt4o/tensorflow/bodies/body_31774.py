# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/nth_element_op_test.py
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "non-negative but is -1"):
    nn_ops.nth_element([5], -1)
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "scalar but has rank 1"):
    nn_ops.nth_element([5, 6, 3], [1])

# Test with placeholders
with ops.Graph().as_default():
    with self.session(use_gpu=False):
        n = array_ops.placeholder(dtypes.int32)
        values = nn_ops.nth_element([5], n)
        with self.assertRaisesOpError("non-negative but is -1"):
            values.eval(feed_dict={n: -1})
