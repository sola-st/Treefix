# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
super().__init__(wall_time, locator)
self._graph_id = graph_id
self._op_type = op_type
self._op_name = op_name
self._output_tensor_ids = _tuple_or_none(output_tensor_ids)
self._host_name = host_name
self._stack_frame_ids = stack_frame_ids
self._input_names = _tuple_or_none(input_names)
self._device_name = device_name
