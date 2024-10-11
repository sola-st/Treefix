# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/tracing_compiler.py
"""Returns a concrete function which cleans up its graph function."""
with self._lock:
    concrete_function, _ = self._maybe_define_concrete_function(args, kwargs)
exit(concrete_function)
