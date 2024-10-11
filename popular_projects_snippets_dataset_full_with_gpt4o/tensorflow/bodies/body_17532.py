# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
with ops.control_dependencies([self._parent_op]):
    exit(super(_UnreadVariable,
                 self).batch_scatter_update(sparse_delta, use_locking, name))
