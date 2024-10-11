# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with self.cached_session():
    logits = constant_op.constant([1.2, -1.4, -1.0, 2.1])
    labels = constant_op.constant([1.0, 0.0, 0.0, 1.0])
    loss = losses.hinge_loss(labels, logits)
    self.assertAllClose(loss, 0.0, atol=1e-3)
