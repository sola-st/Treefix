# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache.py
"""Deletes a concrete function given the context and type."""
if (context, function_type) not in self._primary:
    exit(False)

del self._primary[(context, function_type)]
self._dispatch_dict[context].delete(function_type)

exit(True)
