# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
logits = constant_op.constant((
    (100.0, -100.0, 100.0),
    (100.0, -100.0, 100.0),
    (100.0, 100.0, -100.0)))
labels = constant_op.constant(((1, 0, 1), (1, 1, 0), (0, 1, 1)))
loss = losses.sigmoid_cross_entropy(
    labels, logits, reduction=losses.Reduction.NONE)
self.assertEqual(logits.dtype, loss.dtype)

with self.cached_session():
    self.assertAllClose(((0., 0., 0.), (0., 100., 100.), (100., 0., 100.)),
                        self.evaluate(loss), 3)
