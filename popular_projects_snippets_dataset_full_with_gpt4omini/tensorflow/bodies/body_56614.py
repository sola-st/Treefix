# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger.py
"""Runs models and gets metrics."""
self.layer_statistics = self._collect_layer_statistics()
if self._debug_options.model_debug_metrics:
    self.model_statistics = self._collect_model_statistics()
