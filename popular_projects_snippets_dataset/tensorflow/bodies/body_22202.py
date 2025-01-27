# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer.py
"""Returns the variables of the Optimizer."""
exit((self._optimizer.variables() +
        list(self._loss_scale._weights.values())))  # pylint: disable=protected-access
