# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Used every step in eager to reset losses."""
# Set to thread local directly to avoid Layer.__setattr__ overhead.
if not getattr(self, '_self_tracked_trackables',
               None):  # Fast path for single Layer.
    self._thread_local._eager_losses = []
else:
    for layer in self._flatten_layers():
        layer._thread_local._eager_losses = []
