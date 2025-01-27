# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
for reduction in losses.Reduction.all():
    with ops.Graph().as_default() as g:
        self.assertEqual(0, len(util.get_losses()))
        raw_losses = self._raw_losses
        unweighted_losses = (
            losses.compute_weighted_loss(raw_losses, reduction=reduction),
            losses.compute_weighted_loss(
                raw_losses, weights=np.ones((1, 1, 1)), reduction=reduction),
            losses.compute_weighted_loss(
                raw_losses, weights=np.ones((1, 1, 4)), reduction=reduction),
            losses.compute_weighted_loss(
                raw_losses, weights=np.ones((1, 2, 1)), reduction=reduction),
            losses.compute_weighted_loss(
                raw_losses, weights=np.ones((1, 2, 4)), reduction=reduction),
            losses.compute_weighted_loss(
                raw_losses, weights=np.ones((3, 1, 1)), reduction=reduction),
            losses.compute_weighted_loss(
                raw_losses, weights=np.ones((3, 1, 4)), reduction=reduction),
            losses.compute_weighted_loss(
                raw_losses, weights=np.ones((3, 2, 1)), reduction=reduction),
            losses.compute_weighted_loss(
                raw_losses, weights=np.ones(self._shape), reduction=reduction)
        )
        self.assertEqual(9, len(util.get_losses()))
        with self.session(g):
            for unweighted_loss in unweighted_losses:
                if reduction == losses.Reduction.NONE:
                    self.assertAllClose(self._raw_losses,
                                        self.evaluate(unweighted_loss))
                elif reduction == losses.Reduction.SUM:
                    self.assertAllClose(
                        np.sum(self._raw_losses), self.evaluate(unweighted_loss))
                else:
                    # reduction one of MEAN, SUM_OVER_NONZERO_WEIGHTS,
                    # SUM_BY_NONZERO_WEIGHTS or SUM_OVER_BATCH_SIZE.
                    self.assertAllClose(
                        np.mean(self._raw_losses), self.evaluate(unweighted_loss))
