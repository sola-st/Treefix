# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_xent_test.py
with self.cached_session():
    logits = constant_op.constant([0.0, 0.0], dtype=dtypes.float64)
    targets = constant_op.constant([0.0, 1.0], dtype=dtypes.float64)
    loss = nn_impl.sigmoid_cross_entropy_with_logits(
        labels=targets, logits=logits)
    grads = gradients_impl.gradients(loss, logits)[0].eval()
self.assertAllClose(grads, [0.5, -0.5])
