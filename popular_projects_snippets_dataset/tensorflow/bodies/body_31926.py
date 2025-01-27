# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
for reduction in losses.Reduction.all():
    with ops.Graph().as_default() as g:
        self.assertEqual(0, len(util.get_losses()))
        weighted_loss = losses.compute_weighted_loss(
            self._raw_losses, weights=weights, reduction=reduction)
        self.assertEqual(1, len(util.get_losses()))
        with self.session(g):
            weighted_losses = weights * self._raw_losses
            weighted_sum = np.sum(weighted_losses)
            if reduction == losses.Reduction.NONE:
                self.assertAllClose(weighted_losses, self.evaluate(weighted_loss))
            elif reduction == losses.Reduction.SUM:
                self.assertAllClose(weighted_sum, self.evaluate(weighted_loss))
            else:
                broadcast_weights = weights * np.ones_like(self._raw_losses)
                if reduction == losses.Reduction.MEAN:
                    self.assertAllClose(weighted_sum / np.sum(broadcast_weights),
                                        self.evaluate(weighted_loss))
                elif (reduction == losses.Reduction.SUM_OVER_NONZERO_WEIGHTS or
                      reduction == losses.Reduction.SUM_BY_NONZERO_WEIGHTS):
                    self.assertAllClose(
                        weighted_sum / np.count_nonzero(broadcast_weights),
                        self.evaluate(weighted_loss))
                elif reduction == losses.Reduction.SUM_OVER_BATCH_SIZE:
                    self.assertAllClose(weighted_sum / self._raw_losses.size,
                                        self.evaluate(weighted_loss))
