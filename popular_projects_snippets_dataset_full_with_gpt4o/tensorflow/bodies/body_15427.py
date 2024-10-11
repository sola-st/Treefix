# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""Reverses a RaggedTensor along the specified axes.

  #### Example:

  >>> data = tf.ragged.constant([
  ...   [[1, 2], [3, 4]], [[5, 6]], [[7, 8], [9, 10], [11, 12]]])
  >>> tf.reverse(data, axis=[0, 2])
  <tf.RaggedTensor [[[8, 7], [10, 9], [12, 11]], [[6, 5]], [[2, 1], [4, 3]]]>

  Args:
    tensor: A 'RaggedTensor' to reverse.
    axis: A list or tuple of 'int' or a constant 1D 'tf.Tensor'. The indices of
      the axes to reverse.
    name: A name prefix for the returned tensor (optional).

  Returns:
    A 'RaggedTensor'.
  """
type_error_msg = ('`axis` must be a list of int or a constant tensor'
                  'when reversing axes in a ragged tensor')

with ops.name_scope(name, 'Reverse', [tensor, axis]):
    if isinstance(axis, ops.Tensor):
        axis = tensor_util.constant_value(axis)
        if axis is None:
            raise TypeError(type_error_msg)
    elif not (isinstance(axis, (list, tuple)) and
              all(isinstance(dim, int) for dim in axis)):
        raise TypeError(type_error_msg)

    tensor = ragged_tensor.convert_to_tensor_or_ragged_tensor(
        tensor, name='tensor')

    # Allow usage of negative values to specify innermost axes.
    axis = [
        array_ops.get_positive_axis(dim, tensor.shape.rank, 'axis[%d]' % i,
                                    'rank(tensor)')
        for i, dim in enumerate(axis)
    ]

    # We only need to slice up to the max axis. If the axis list
    # is empty, it should be 0.
    slices = [slice(None)] * (max(axis) + 1 if axis else 0)

    for dim in axis:
        slices[dim] = slice(None, None, -1)

    exit(tensor[tuple(slices)])
