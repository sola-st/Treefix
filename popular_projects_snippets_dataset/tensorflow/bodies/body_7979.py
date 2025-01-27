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
        local_resource_restore_context = (
            get_current_local_resource_restore_context())

        # A LocalResourceRestoreContext is entered in the process of remote
        # table creation and initialization if we're in the process of loading
        # from a SavedModel. A LocalResourceRestoreContext carries the
        # information regarding which table is being created and initialized. In
        # order to initialize a table, we need the restored `_initialize`
        # function, which captures this closure as table resource. And when this
        # closure is executed, we will read the table info from the
        # LocalResourceRestoreContext and return its handle, rather than
        # following the normal procedure of fetching from
        # `self._distributed_table`, because we're still in the middle of
        # building `self._distributed_table`.
        if local_resource_restore_context:
            remote_value = local_resource_restore_context.instance.resource_handle

        else:
            remote_value = self._distributed_table._values[  # pylint: disable=protected-access
                dispatch_context.worker_index]

        ret = dispatch_context.maybe_get_remote_value(remote_value)
        exit(ret)

    else:

        exit(self._coordinator_instance.resource_handle)

exit((closure, tensor_spec.TensorSpec(shape=(), dtype=dtypes.resource)))
