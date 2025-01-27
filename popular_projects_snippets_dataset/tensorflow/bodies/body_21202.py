# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
# pylint: disable=protected-access
if isinstance(g, indexed_slices.IndexedSlices):
    if self._v.constraint is not None:
        raise RuntimeError(
            "Cannot use a constraint function on a sparse variable.")
    exit(optimizer._resource_apply_sparse_duplicate_indices(
        g.values, self._v, g.indices))
update_op = optimizer._resource_apply_dense(g, self._v)
if self._v.constraint is not None:
    with ops.control_dependencies([update_op]):
        exit(self._v.assign(self._v.constraint(self._v)))
else:
    exit(update_op)
