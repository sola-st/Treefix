# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Resets the state of loss metrics."""
if not self._built:
    exit()
metrics = [self._loss_metric] + nest.flatten(self._per_output_metrics)
for metric_obj in metrics:
    if metric_obj is not None:
        metric_obj.reset_state()
