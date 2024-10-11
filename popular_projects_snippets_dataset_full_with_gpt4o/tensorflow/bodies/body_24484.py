# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
super().__init__(
    execution_digest.wall_time,
    execution_digest.locator,
    execution_digest.op_type,
    output_tensor_device_ids=execution_digest.output_tensor_device_ids)
self._host_name = host_name
self._stack_frame_ids = tuple(stack_frame_ids)
self._tensor_debug_mode = tensor_debug_mode
self._graph_id = graph_id
self._input_tensor_ids = _tuple_or_none(input_tensor_ids)
self._output_tensor_ids = _tuple_or_none(output_tensor_ids)
self._debug_tensor_values = _tuple_or_none(debug_tensor_values)
