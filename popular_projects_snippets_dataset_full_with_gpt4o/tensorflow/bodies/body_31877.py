# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with self.cached_session():
    self.assertEqual(
        0.0,
        losses.mean_squared_error(predictions=constant_op.constant(0),
                                  labels=constant_op.constant(0)).eval())
