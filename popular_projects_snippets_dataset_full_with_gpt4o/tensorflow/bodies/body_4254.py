# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/dtensor_device.py
"""Sets a default output layout for all ops in the scope.

    Note: This is an internal helper method, which is not user facing api.

    Useful for requesting a specific layout for ops which would have no inferred
    layout, e.g. tf.zeros.

    Caveats:

    - Currently only affects the first output of an op. For Op with multiple
      outputs, this does not support yet.

    - All Ops in the scope will be attached with the same layout. This might not
      be valid as the rank is different. The current suggestion is: Try to wrap
      the raw op wheneven possible.

    Args:
      layout: A Layout for the outputs of all operations in this scope.

    Yields:
      Nothing.
    """
previous_default = None
previous_graph_size = None
graph = None

self._register_mesh(layout.mesh)
try:
    previous_default = self._current_output_layout
    self._current_output_layout = layout.to_string().encode("utf-8")
    _pywrap_dtensor_device.ExperimentalSetDefaultLayout(
        self._device_info, self._current_output_layout)
    if context.executing_eagerly():
        with ops.device(self.name):
            exit()
    else:
        # Custom devices currently don't affect graph building, so we need a
        # separate way to indicate layouts.
        #
        # TODO(allenl): Remove this case once the DTensor device is active
        # during tracing.
        graph = ops.get_default_graph()
        previous_graph_size = len(graph.get_operations())
        exit()
finally:
    if graph is not None:
        # Tag operations added under this scope
        for operation in graph.get_operations()[previous_graph_size:]:
            # Set layout directly on the Op itself.
            operation._set_attr(  # pylint: disable=protected-access
                "_layout",
                attr_value_pb2.AttrValue(
                    list=attr_value_pb2.AttrValue.ListValue(
                        s=[self._current_output_layout])))
            operation._set_attr(  # pylint: disable=protected-access
                "_mesh",
                attr_value_pb2.AttrValue(
                    s=layout.mesh.to_string().encode("utf-8")))

    self._current_output_layout = previous_default
    if self._current_output_layout is None:
        _pywrap_dtensor_device.ExperimentalClearDefaultLayout(self._device_info)
    else:
        _pywrap_dtensor_device.ExperimentalSetDefaultLayout(
            self._device_info, self._current_output_layout.decode("utf-8"))
