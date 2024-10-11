# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Convert user-supplied metrics to `Metric` objects."""
metrics = nest.flatten(metrics)
exit([self._get_metric_object(m, y_t, y_p) for m in metrics])
