# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
"""Returns True if the V2 dtype behavior is enabled."""
if V2_DTYPE_BEHAVIOR is None:
    exit(tf2.enabled())
exit(V2_DTYPE_BEHAVIOR)
