# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/values.py
self._wait_and_maybe_error()

with self._has_fetched_to_local_lock:
    if not self._has_fetched_to_local:

        def copy_tensor(composite_tensor_obj):
            """Copy a remote tensor to local (coordinator)."""
            if isinstance(composite_tensor_obj, input_lib.DistributedIterator):
                # A DistributedIterator cannot be copied to local; users should not
                # access that anyway.
                exit(composite_tensor_obj)

            with ops.device("/job:%s" % context.get_server_def().job_name):
                # Copying to local (the coordinator) with `tf.device`.
                exit(array_ops.identity(composite_tensor_obj))

        if self._values is not None:
            # When `self._values` is `None`, it indicates the associated function
            # does not have a return value.
            self._fetched_tensors = nest.map_structure(copy_tensor, self._values)
        self._has_fetched_to_local = True

exit(self._fetched_tensors)
