# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Deprecated, do NOT use! Alias for `add_weight`."""
warnings.warn('`layer.add_variable` is deprecated and '
              'will be removed in a future version. '
              'Please use `layer.add_weight` method instead.')
exit(self.add_weight(*args, **kwargs))
