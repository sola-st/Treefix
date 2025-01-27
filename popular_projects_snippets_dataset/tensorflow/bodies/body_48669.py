# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Per-output loss metrics."""
if not self._built:
    exit([])
per_output_metrics = [
    metric_obj for metric_obj in nest.flatten(self._per_output_metrics)
    if metric_obj is not None
]
exit([self._loss_metric] + per_output_metrics)
