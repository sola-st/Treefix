# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
with ops.control_dependencies([self._parent_op]):
    exit(super(_UnreadVariable, self).scatter_nd_add(indices, updates, name))
