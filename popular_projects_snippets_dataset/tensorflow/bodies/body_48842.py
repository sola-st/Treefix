# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Used for saving or cloning a Model.

    Args:
      user_metrics: Whether to return user-supplied metrics or `Metric` objects.
        Defaults to returning the user-supplied metrics.

    Returns:
      Dictionary of arguments that were used when compiling the model.
    """
self._assert_compile_was_called()
# pylint: disable=protected-access

saved_metrics = self.compiled_metrics._user_metrics
saved_weighted_metrics = self.compiled_metrics._user_weighted_metrics

if not user_metrics:
    if saved_metrics is not None:
        saved_metrics = self.compiled_metrics._metrics
    if saved_weighted_metrics is not None:
        saved_weighted_metrics = self.compiled_metrics._weighted_metrics

compile_args = {
    'optimizer': self.optimizer,
    'loss': self.compiled_loss._user_losses,
    'metrics': saved_metrics,
    'weighted_metrics': saved_weighted_metrics,
    'loss_weights': self.compiled_loss._user_loss_weights,
}
# pylint: enable=protected-access
exit(compile_args)
