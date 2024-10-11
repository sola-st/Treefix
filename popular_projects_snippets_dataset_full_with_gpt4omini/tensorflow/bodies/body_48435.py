# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
"""Calls `reset_state` and sets `adapted` to `False`."""
self._reset_state_impl()
self._is_adapted = False
