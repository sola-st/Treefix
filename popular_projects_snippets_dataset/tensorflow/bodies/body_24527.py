# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
super().__init__(graph_execution_trace_digest.wall_time,
                 graph_execution_trace_digest.locator,
                 graph_execution_trace_digest.op_type,
                 graph_execution_trace_digest.op_name,
                 graph_execution_trace_digest.output_slot,
                 graph_execution_trace_digest.graph_id)
self._graph_ids = tuple(graph_ids)
self._tensor_debug_mode = tensor_debug_mode
self._debug_tensor_value = debug_tensor_value
self._device_name = device_name
