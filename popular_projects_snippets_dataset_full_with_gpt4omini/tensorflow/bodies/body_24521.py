# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
super().__init__(wall_time, locator)
self._op_type = op_type
self._op_name = op_name
self._output_slot = output_slot
self._graph_id = graph_id
