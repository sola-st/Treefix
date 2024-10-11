# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_loss_scaling_utilities_test.py
with self.assertRaisesIncompatibleShapesError(
    (ValueError, errors_impl.InvalidArgumentError)):
    nn_impl.compute_average_loss([2.5, 6.2, 5.],
                                 sample_weight=[0.2, 0.8],
                                 global_batch_size=10)
