# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with ops.Graph().as_default():
    self.assertEqual(0, len(util.get_losses()))
    weight = 17.0
    weighted_loss = losses.compute_weighted_loss(
        self._raw_losses, weights=weight)
    self.assertEqual(1, len(util.get_losses()))
    with self.cached_session():
        self.assertAllClose(
            np.mean(weight * self._raw_losses), self.evaluate(weighted_loss))
