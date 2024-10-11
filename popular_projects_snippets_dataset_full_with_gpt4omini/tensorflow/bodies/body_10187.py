# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_loss_scaling_utilities_test.py
with distribution.scope():
    with self.assertRaisesRegex(
        RuntimeError, "You are calling `scale_regularization_loss` in "
        "cross replica context"):
        nn_impl.scale_regularization_loss([2, 3])
