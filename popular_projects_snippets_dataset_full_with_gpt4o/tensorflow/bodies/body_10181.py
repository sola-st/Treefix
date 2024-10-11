# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_loss_scaling_utilities_test.py
with distribution.scope():
    # Scalar sample weight
    per_replica_losses = distribution.run(
        nn_impl.compute_average_loss,
        args=([2., 4., 6.],),
        kwargs={"sample_weight": 2})
    loss = distribution.reduce("SUM", per_replica_losses, axis=None)
    self.assertAllClose(self.evaluate(loss), (2. + 4. + 6.) * 2. / 3)

    # Per example sample weight
    per_replica_losses = distribution.run(
        nn_impl.compute_average_loss,
        args=([2., 4., 6.],),
        kwargs={"sample_weight": [0.3, 0.5, 0.2]})
    loss = distribution.reduce("SUM", per_replica_losses, axis=None)
    self.assertAllClose(
        self.evaluate(loss), (2. * 0.3 + 4. * 0.5 + 6. * 0.2) / 3)

    # Time-step sample weight
    per_replica_losses = distribution.run(
        nn_impl.compute_average_loss,
        args=([[2., 0.5], [4., 1.]],),
        kwargs={"sample_weight": [[0.3, 0.7], [0.2, 0.8]]})
    loss = distribution.reduce("SUM", per_replica_losses, axis=None)
    self.assertAllClose(
        self.evaluate(loss), (2. * 0.3 + 0.5 * 0.7 + 4. * 0.2 + 1. * 0.8) / 2)
