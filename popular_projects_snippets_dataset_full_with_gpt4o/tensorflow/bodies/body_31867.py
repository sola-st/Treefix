# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with self.cached_session():
    logits = constant_op.constant([[-0.7], [-1.4], [1.4], [0.6]])
    labels = constant_op.constant([[0.0], [0.0], [1.0], [1.0]])
    loss = losses.hinge_loss(labels, logits)
    # Examples 1 and 4 are on the correct side of the hyperplane but within
    # the margin so they incur some (small) loss.
    self.assertAllClose(loss, 0.175, atol=1e-3)
