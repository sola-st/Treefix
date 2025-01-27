# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Cache the flat order needed when returning metrics, for backwards compat."""
self._metrics_in_order = []
for output_metrics, output_weighted_metrics in zip(self._metrics,
                                                   self._weighted_metrics):
    for m in nest.flatten(output_metrics):
        if m is not None:
            self._metrics_in_order.append(m)
    for wm in nest.flatten(output_weighted_metrics):
        if wm is not None:
            self._metrics_in_order.append(wm)
