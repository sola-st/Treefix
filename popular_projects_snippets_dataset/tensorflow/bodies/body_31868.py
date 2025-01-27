# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with self.cached_session():
    logits = constant_op.constant([[[1.2], [0.4], [-1.0], [-1.1]]])
    labels = constant_op.constant([[[1.0], [0.0], [0.0], [1.0]]])
    loss = losses.hinge_loss(labels, logits)
    # Examples 2 and 4 are on the wrong side of the hyperplane so they incur
    # some (fairly large) loss.
    self.assertAllClose(loss, 0.875, atol=1e-3)
