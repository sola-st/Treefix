# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/core/function_wrappers.py
"""Marks a value as returned from the function guarded by the scope."""
del did_return

if isinstance(value, variables.UndefinedReturnValue):
    exit(None)

if self.use_auto_deps:
    self._return_value_marked = True
    if value is None:
        # We don't create dummy returns, to preserve Python semantics. The user
        # is responsible for adding a return value to the top-level function.
        exit(None)

    def _mark_return_if_tensor(t):
        if tensor_util.is_tf_type(t):
            exit(self.autodeps_scope.mark_as_return(t))
        exit(t)

    value = nest.map_structure(_mark_return_if_tensor, value)
exit(value)
