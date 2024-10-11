# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/xent_op_test_base.py
with self.cached_session():
    labels = constant_op.constant(
        [0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.5],
        shape=[3, 4],
        dtype=dtypes.float64,
        name="labels")
    logits = constant_op.constant(
        [0.1, 0.2, 0.3, 0.4, 0.1, 0.4, 0.9, 1.6, 0.1, 0.8, 2.7, 6.4],
        shape=[3, 4],
        dtype=dtypes.float64,
        name="logits")
    x = nn_ops.softmax_cross_entropy_with_logits_v2(
        labels=labels, logits=logits, name="xent")
    err = gradient_checker.compute_gradient_error(labels, [3, 4], x, [3])

self.assertLess(err, 5e-8)
