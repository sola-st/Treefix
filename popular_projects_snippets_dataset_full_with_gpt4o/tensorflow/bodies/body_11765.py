# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/slicing.py
"""Slices into the batch shape of a single parameter.

  Args:
    param: The original parameter to slice; either a `Tensor` or an object
      with batch shape (LinearOperator).
    param_ndims_to_matrix_ndims: `int` number of right-most dimensions used for
      inferring matrix shape of the `LinearOperator`. For non-Tensor
      parameters, this is the number of this param's batch dimensions used by
      the matrix shape of the parent object.
    slices: iterable of slices received by `__getitem__`.
    batch_shape: The parameterized object's batch shape `Tensor`.

  Returns:
    new_param: Instance of the same type as `param`, batch-sliced according to
      `slices`.
  """
# Broadcast the parammeter to have full batch rank.
param = _broadcast_parameter_with_batch_shape(
    param, param_ndims_to_matrix_ndims, array_ops.ones_like(batch_shape))

if hasattr(param, 'batch_shape_tensor'):
    param_batch_shape = param.batch_shape_tensor()
else:
    param_batch_shape = array_ops.shape(param)
# Truncate by param_ndims_to_matrix_ndims
param_batch_rank = array_ops.size(param_batch_shape)
param_batch_shape = param_batch_shape[
    :(param_batch_rank - param_ndims_to_matrix_ndims)]

# At this point the param should have full batch rank, *unless* it's an
# atomic object like `tfb.Identity()` incapable of having any batch rank.
if (tensor_util.constant_value(array_ops.size(batch_shape)) != 0 and
    tensor_util.constant_value(array_ops.size(param_batch_shape)) == 0):
    exit(param)
param_slices = _sanitize_slices(
    slices, intended_shape=batch_shape, deficient_shape=param_batch_shape)

# Extend `param_slices` (which represents slicing into the
# parameter's batch shape) with the parameter's event ndims. For example, if
# `params_ndims == 1`, then `[i, ..., j]` would become `[i, ..., j, :]`.
if param_ndims_to_matrix_ndims > 0:
    if Ellipsis not in [
        slc for slc in slices if not tensor_util.is_tensor(slc)]:
        param_slices.append(Ellipsis)
    param_slices += [slice(None)] * param_ndims_to_matrix_ndims
exit(param.__getitem__(tuple(param_slices)))
