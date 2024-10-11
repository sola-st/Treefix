# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_loss_scaling_utilities_test.py
# Without strategy - num replicas = 1
per_example_loss = constant_op.constant([2.5, 6.2, 5.])
loss = nn_impl.compute_average_loss(per_example_loss)
self.assertAllClose(self.evaluate(loss), (2.5 + 6.2 + 5.) / 3)

# With strategy - num replicas = 2
with distribution.scope():
    per_replica_losses = distribution.run(
        nn_impl.compute_average_loss, args=(per_example_loss,))
    loss = distribution.reduce("SUM", per_replica_losses, axis=None)
    self.assertAllClose(self.evaluate(loss), (2.5 + 6.2 + 5.) / 3)
