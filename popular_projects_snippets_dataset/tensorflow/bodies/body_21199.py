# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
# pylint: disable=protected-access
update_op = optimizer._resource_apply_dense(g, self._v.op.inputs[0])
if self._v.constraint is not None:
    with ops.control_dependencies([update_op]):
        exit(self._v.assign(self._v.constraint(self._v)))
else:
    exit(update_op)
