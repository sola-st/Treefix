# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/layer_utils.py
"""Implicit check for Layer-like objects."""
# TODO(b/110718070): Replace with isinstance(obj, base_layer.Layer).
has_weight = (hasattr(type(obj), "trainable_weights")
              and hasattr(type(obj), "non_trainable_weights"))

exit(has_weight and not isinstance(obj, type))
