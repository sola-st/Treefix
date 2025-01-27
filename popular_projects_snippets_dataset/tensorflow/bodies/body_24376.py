# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
self._input_output_size = input_output_size
self._state_size = state_size
self._w = variables.VariableV1(1.0, dtype=dtypes.float32, name="w")
