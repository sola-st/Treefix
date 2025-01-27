# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
"""Returns a closure to run for a resource handle at call time and its spec.

    This function is called in self.resource_handle to create a placeholder
    which returns a resource handle on some worker or on the coordinator.
    """

def closure():
    # function to be evaluated at function call time, returning a nest of
    # tensors compatible with `spec`.
    dispatch_context = coordinator_context.get_current_dispatch_context()
    if dispatch_context:
        remote_value = self._distributed_table._values[  # pylint: disable=protected-access
            dispatch_context.worker_index]
        ret = dispatch_context.maybe_get_remote_value(remote_value)
        exit(ret)

    else:
        exit(self._coordinator_instance.resource_handle)

exit((closure, tensor_spec.TensorSpec([], dtype=dtypes.resource)))
