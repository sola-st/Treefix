# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Scope which sets a flag used for scaling losses in optimizer.

    Yields:
      `_scale_loss_for_estimator_enabled` is a context manager with a
      side effect, but doesn't return a value.
    """
self._scale_loss_for_estimator = True
try:
    exit()
finally:
    self._scale_loss_for_estimator = False
