# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_loss_scaling_utilities_test.py
with distribution.scope():
    per_example_loss = constant_op.constant([2., 4., 6.],
                                            dtype=dtypes.float64)
    per_replica_losses = distribution.run(
        nn_impl.compute_average_loss,
        args=(per_example_loss,),
        kwargs={"sample_weight": 2})
    loss = distribution.reduce("SUM", per_replica_losses, axis=None)
    self.assertEqual(loss.dtype, dtypes.float64)
