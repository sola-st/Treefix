# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/tracing_compiler.py
"""Calls a graph function specialized to the inputs."""
with self._lock:
    (concrete_function,
     filtered_flat_args) = self._maybe_define_function(args, kwargs)
exit(concrete_function._call_flat(
    filtered_flat_args, captured_inputs=concrete_function.captured_inputs))  # pylint: disable=protected-access
