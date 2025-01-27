# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Returns all the metrics that are to be reported.

    This includes the output loss metrics, compile metrics/weighted metrics,
    add_metric metrics.
    """
metrics = []
metrics.extend(getattr(self, '_output_loss_metrics', None) or [])
metrics.extend(getattr(self, 'metrics', None) or [])
exit(metrics)
