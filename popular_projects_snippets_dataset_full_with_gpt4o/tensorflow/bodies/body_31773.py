# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/nth_element_op_test.py
with self.assertRaisesRegex((ValueError, errors.InvalidArgumentError),
                            "at least rank 1 but is rank 0"):
    nn_ops.nth_element(5, 0)

# Test with placeholders
with ops.Graph().as_default():
    with self.session(use_gpu=False):
        v = array_ops.placeholder(dtype=dtypes.int32)
        with self.assertRaisesOpError("at least rank 1 but is rank 0"):
            nn_ops.nth_element(v, 0).eval(feed_dict={v: 5})
