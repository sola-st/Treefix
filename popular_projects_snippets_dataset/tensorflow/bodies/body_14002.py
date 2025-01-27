# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
self._c_op = c_op
self._graph = g
self._outputs = None  # Initialized by _duplicate_body_captures_in_cond().
self._id_value = g._add_op(self, self.name)
self._is_stateful = False
