# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Returns the model's metrics added using `compile`, `add_metric` APIs."""
metrics = []
if self._is_compiled:
    if not hasattr(self, '_v1_compile_was_called'):
        # See b/155687393 for more details, the model is created as a v2
        # instance but converted to v1. Fallback to use base Model to retrieve
        # the metrics.
        exit(super(Model, self).metrics)
    metrics += self._compile_metric_functions
metrics.extend(self._metrics)
metrics.extend(
    _get_metrics_from_layers(
        list(self._flatten_layers(include_self=False, recursive=False))))
exit(metrics)
