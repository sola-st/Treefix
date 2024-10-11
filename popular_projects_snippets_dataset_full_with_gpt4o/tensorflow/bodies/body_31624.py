# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
with self.cached_session(use_gpu=test.is_gpu_available()):
    t = constant_op.constant(1.0, shape=[1, 1, 1, 1])
    with self.assertRaisesRegex(
        (errors_impl.InvalidArgumentError, ValueError),
        "Negative dimension size"):
        t = self.evaluate(
            nn_ops.max_pool(t, ksize=[1, 1, 2, 1], strides=1, padding="VALID"))
