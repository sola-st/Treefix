# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_loss_scaling_utilities_test.py
with distribution.scope():
    with self.assertRaisesRegex(
        RuntimeError,
        "You are calling `compute_average_loss` in cross replica context"):
        nn_impl.compute_average_loss([2, 3])
