# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/testing.py
super().setUp()
self.variables = {}
self.trace_log = []
self.raises_cm = None
op_callbacks.add_op_callback(self._op_callback)
