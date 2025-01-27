# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Resets the state of all `Metric`s in this container."""
if self._built:
    metrics = self._metrics_in_order
else:
    # If the user supplied `Metric` objects directly, we should
    # reset those. This could also contain `str`s or `function`s
    # though.
    metrics = nest.flatten(self._user_metrics) + nest.flatten(
        self._user_weighted_metrics)

for metric_obj in metrics:
    if isinstance(metric_obj, metrics_mod.Metric):
        metric_obj.reset_state()
