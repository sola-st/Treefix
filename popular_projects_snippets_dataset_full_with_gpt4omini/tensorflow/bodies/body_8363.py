# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
"""Returns the next instance key."""
if self._use_unique_instance_key():
    # Assigning instance keys at function building time have issues since
    # different workers may retrace the function at different times. With
    # collective V2 we can use capture_call_time_value to use a placeholder as
    # the instance key and feed it at function call time. In this way we also
    # don't reuse instance keys, which allows for per-instance cancellation.
    graph = ops.get_default_graph()
    # Control flow ops don't work with capture_call_time_value, so we put the
    # capture in the function graph of that control flow op.
    while getattr(graph, 'is_control_flow_graph', False):
        graph = graph.outer_graph
    if not context.executing_eagerly() and graph.building_function:
        with graph.as_default():
            # Capture self._next_instance_key so that when building a function
            # that calls another tf.function, the instance key assignment is
            # further delayed until we actually call the function in eager. Note
            # that capture_call_time_value doesn't automatically propagate the
            # deferred capture to the outer function.
            exit(graph.capture_call_time_value(
                self._next_instance_key, tensor_spec.TensorSpec([], dtypes.int32)))
    else:
        instance_key = self._collective_keys.get_instance_key(
            self._group_key, self._device)
        with ops.device('CPU:0'):
            exit(ops.convert_to_tensor(instance_key, dtype=dtypes.int32))
else:
    exit(self._collective_keys.get_instance_key(self._group_key,
                                                  self._device))
