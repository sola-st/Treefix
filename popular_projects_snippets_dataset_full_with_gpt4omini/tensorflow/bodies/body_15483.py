# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_gather_ops.py
"""Gathers ragged slices from `params` axis `0` according to `indices`.

  See `tf.gather` for full documentation.  (This version has the same API
  as `tf.gather`, but supports ragged `params` and `indices`.)

  Examples:

  >>> params = tf.constant(['a', 'b', 'c', 'd', 'e'])
  >>> indices = tf.constant([3, 1, 2, 1, 0])
  >>> ragged_params = tf.ragged.constant([['a', 'b', 'c'], ['d'], [], ['e']])
  >>> ragged_indices = tf.ragged.constant([[3, 1, 2], [1], [], [0]])

  >>> tf.gather(params, ragged_indices)
  <tf.RaggedTensor [[b'd', b'b', b'c'], [b'b'], [], [b'a']]>

  >>> tf.gather(ragged_params, indices)
  <tf.RaggedTensor [[b'e'], [b'd'], [], [b'd'], [b'a', b'b', b'c']]>

  >>> tf.gather(ragged_params, ragged_indices)
  <tf.RaggedTensor [[[b'e'], [b'd'], []], [[b'd']], [], [[b'a', b'b', b'c']]]>

  Args:
    params: The potentially ragged tensor from which to gather values. Must be
      at least rank 1.
    indices: The potentially ragged tensor indicating which values to gather.
      Must have dtype `int32` or `int64`.  Values must be in the range `[0,
      params.shape[0]]`.
    validate_indices: Ignored.
    axis: The axis in `params` to gather `indices` from.
    batch_dims: The number of batch dimensions.
    name: A name for the operation (optional).

  Returns:
    A `RaggedTensor`, where `output.dtype=params.dtype` and
    `output.shape=indices.shape + params.shape[1:]` and
    `output.ragged_rank=indices.shape.ndims + params.ragged_rank`.

  Raises:
    ValueError: If indices.shape.ndims is not known statically.
  """
del validate_indices

with ops.name_scope(name, 'RaggedGather', [params, indices]):
    params = ragged_tensor.convert_to_tensor_or_ragged_tensor(
        params, name='params')
    indices = ragged_tensor.convert_to_tensor_or_ragged_tensor(
        indices, name='indices')
    params, indices = ragged_tensor.match_row_splits_dtypes(params, indices)

    if batch_dims != indices.shape.rank:
        batch_dims = array_ops.get_positive_axis(
            batch_dims,
            indices.shape.rank,
            axis_name='batch_dims',
            ndims_name='rank(indices)')
    if params.shape.rank is not None and batch_dims >= params.shape.rank:
        raise ValueError('batch_dims must be less than rank(params)')
    if axis is None:
        axis = batch_dims
    axis = array_ops.get_positive_axis(
        axis, params.shape.rank, ndims_name='rank(params)')
    if axis < batch_dims:
        raise ValueError('axis must be greater than or equal to batch_dims')
    if indices.shape.rank is not None:
        if not 0 <= batch_dims <= indices.shape.rank:
            raise ValueError(
                'batch_dims=%s must be between 0 and rank(indices)=%s' %
                (batch_dims, indices.shape.rank))

    exit(_gather(params, indices, axis, batch_dims))
