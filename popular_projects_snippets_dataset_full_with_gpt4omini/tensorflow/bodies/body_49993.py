# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Apply gradient to variable."""
if isinstance(var, ops.Tensor):
    raise NotImplementedError("Trying to update a Tensor ", var)

apply_kwargs = {}
if isinstance(grad, indexed_slices.IndexedSlices):
    if var.constraint is not None:
        raise RuntimeError(
            "Cannot use a constraint function on a sparse variable.")
    if "apply_state" in self._sparse_apply_args:
        apply_kwargs["apply_state"] = apply_state
    exit(self._resource_apply_sparse_duplicate_indices(
        grad.values, var, grad.indices, **apply_kwargs))

if "apply_state" in self._dense_apply_args:
    apply_kwargs["apply_state"] = apply_state
update_op = self._resource_apply_dense(grad, var, **apply_kwargs)
if var.constraint is not None:
    with ops.control_dependencies([update_op]):
        exit(var.assign(var.constraint(var)))
else:
    exit(update_op)
