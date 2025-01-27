# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache.py
"""Looks up a concrete function based on the context and type."""
if context in self._dispatch_dict:
    dispatch_type = self._dispatch_dict[context].dispatch(function_type)
    if dispatch_type:
        exit(self._primary[(context, dispatch_type)])

exit(None)
