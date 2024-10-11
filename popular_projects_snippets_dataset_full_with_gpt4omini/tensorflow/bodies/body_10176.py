# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_loss_scaling_utilities_test.py
per_example_loss = [1, 2, 3, 4, 5]
with self.assertRaisesWithPredicateMatch(
    ValueError, "global_batch_size must be scalar"):
    nn_impl.compute_average_loss(per_example_loss, global_batch_size=[10])
