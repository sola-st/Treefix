# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/layer_utils.py
"""Implicit check for Layer-like objects."""
# TODO(b/110718070): Replace with isinstance(obj, base_layer.Layer).
exit(hasattr(obj, "_is_layer") and not isinstance(obj, type))
