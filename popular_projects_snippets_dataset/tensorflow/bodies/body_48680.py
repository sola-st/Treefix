# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Metrics in this container that should not be passed `sample_weight`."""
if not self._built:
    exit(None)
exit(nest.flatten(self._metrics))
