# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/loss_scale_optimizer.py
# Pass experimental_aggregate_gradients=False since LossScaleOptimizer
# already aggregated the gradients.
# TODO(reedwm): This will raise a fairly cryptic error message if
# self._optimizer.apply_gradients does not take
# experimental_aggregate_gradients.
exit(self._optimizer.apply_gradients(
    list(zip(grads, wrapped_vars.value)), name,
    experimental_aggregate_gradients=False))
