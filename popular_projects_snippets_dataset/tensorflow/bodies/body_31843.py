# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
logits = constant_op.constant((
    (100.0, -100.0, 100.0),
    (100.0, -100.0, 100.0),
    (100.0, 100.0, -100.0)
), dtype=dtypes.float64)
labels = constant_op.constant((
    (1, 0, 1), (1, 1, 0), (0, 1, 1)
), dtype=dtypes.int64)
loss = losses.sigmoid_cross_entropy(labels, logits)
self.assertEqual(logits.dtype, loss.dtype)

with self.cached_session():
    self.assertAlmostEqual(44.444, self.evaluate(loss), 3)
