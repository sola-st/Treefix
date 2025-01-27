# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
super().__init__(wall_time, locator)
self._op_type = op_type
self._output_tensor_device_ids = _tuple_or_none(output_tensor_device_ids)
