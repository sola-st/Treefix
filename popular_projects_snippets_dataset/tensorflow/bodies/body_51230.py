# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Attach signature to the root object.

    Args:
      signature_map: An object that contains signature functions.
      wrapped_functions: A dictionary mapping functions to functions that are
        guaranteed to not capture cached variables (functions that capture
        cached variables can't be saved).
    """
self.list_children(self.root)
# Overrides existing dependency.
name = signature_serialization.SIGNATURE_ATTRIBUTE_NAME
self._children_cache[self.root][name] = signature_map
self._wrapped_functions.update(wrapped_functions)
