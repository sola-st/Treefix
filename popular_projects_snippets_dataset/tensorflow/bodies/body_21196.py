# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
if isinstance(g, ops.Tensor):
    update_op = optimizer._apply_dense(g, self._v)  # pylint: disable=protected-access
    if self._v.constraint is not None:
        with ops.control_dependencies([update_op]):
            exit(self._v.assign(self._v.constraint(self._v)))
    else:
        exit(update_op)
else:
    assert isinstance(g, indexed_slices.IndexedSlices), (
        "Gradient ", g, " is neither a tensor nor IndexedSlices.")
    if self._v.constraint is not None:
        raise RuntimeError(
            "Cannot use a constraint function on a sparse variable.")
    # pylint: disable=protected-access
    exit(optimizer._apply_sparse_duplicate_indices(g, self._v))
