# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Creates per-output loss metrics, but only for multi-output Models."""
if len(self._output_names) == 1:
    self._per_output_metrics = [None]
else:
    self._per_output_metrics = []
    for loss_obj, output_name in zip(self._losses, self._output_names):
        if loss_obj is None:
            self._per_output_metrics.append(None)
        else:
            self._per_output_metrics.append(
                metrics_mod.Mean(output_name + '_loss'))
