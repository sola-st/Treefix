# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_utils.py
"""Returns True if `v` is either a PartionedVariable or a ShardedVariable."""
exit(hasattr(v, '_variable_list') or hasattr(v, '_variables'))
