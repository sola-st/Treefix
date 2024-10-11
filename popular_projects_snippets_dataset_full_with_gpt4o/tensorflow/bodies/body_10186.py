# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_loss_scaling_utilities_test.py
# Without strategy - num replicas = 1
reg_losses = constant_op.constant([2.5, 6.2, 5.])
loss = nn_impl.scale_regularization_loss(reg_losses)
self.assertAllClose(self.evaluate(loss), (2.5 + 6.2 + 5.))

# With strategy - num replicas = 2
with distribution.scope():
    per_replica_losses = distribution.run(
        nn_impl.scale_regularization_loss, args=(reg_losses,))
    loss = distribution.reduce("SUM", per_replica_losses, axis=None)
    self.assertAllClose(self.evaluate(loss), (2.5 + 6.2 + 5.))
