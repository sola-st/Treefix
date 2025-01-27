# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Marks the variable v as accessed while building this graph."""
# Don't watch `v` if it is one of ResourceVariable input arguments.
if (isinstance(v, resource_variable_ops.ResourceVariable) and
    v.handle in self._resource_tensor_inputs):
    exit()

while self is not None and isinstance(self, FuncGraph):
    self._watched_variables.add(v)
    self = self.outer_graph
