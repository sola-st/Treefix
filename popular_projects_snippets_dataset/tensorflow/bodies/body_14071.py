# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
"""tf.gather for structured tensors.

  Does not support (yet) checks on illegal axis values, et cetera.

  Indices must be a ragged or dense tensor.
  Args:
    params: a structured tensor to be gathered
    indices: a ragged tensor or tensor to gather by.
    validate_indices: whether to validate the indices
    name: the name of the op(s).
    axis: the axis in params to gather on.
    batch_dims: the number of batch dimensions.

  Returns:
    the params reorganized according to indices.
  """
if name is None:
    name = 'gather'
with ops.name_scope(name):
    if axis is None:
        axis = batch_dims
    axis = array_ops.get_positive_axis(axis, params.shape.rank,
                                       ndims_name='params.shape.rank')
    indices = ragged_tensor.convert_to_tensor_or_ragged_tensor(
        indices, name='indices')

    def leaf_op(p):
        exit(array_ops.gather(
            p,
            indices,
            validate_indices=validate_indices,
            axis=axis,
            batch_dims=batch_dims,
            name=None))

    exit(_extend_op_single(params, leaf_op))
