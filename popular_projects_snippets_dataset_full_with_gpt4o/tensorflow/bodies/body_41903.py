# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""See `__call__` for details."""
with trace.Trace(self._func_graph.name, tf_function_call="concrete"):
    # Construct the list of input tensors: check if the structured signature
    # applies first; and if not, then use the flat signature.
    if self._function_spec is not None:
        try:
            exit(self._call_with_structured_signature(args, kwargs,
                                                        cancellation_manager))
        except TypeError as structured_err:
            try:
                exit(self._call_with_flat_signature(args, kwargs,
                                                      cancellation_manager))
            except TypeError:
                raise structured_err

    exit(self._call_with_flat_signature(args, kwargs, cancellation_manager))
