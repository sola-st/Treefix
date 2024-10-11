# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
"""All-gather a dense tensor.

    This method must be called inside a tf.function.

    Args:
      input_tensor: a dense tensor. It must have the same rank on all replicas,
        and dimensions other than `axis` need to be the same as well.
      axis: 0-D int32 Tensor. Dimension along which to gather. Must be in the
        range [0, rank(value)).
      options: an optional tf.distribute.experimental.CommunicationOptions. If
        provided, it overrides the default options.

    Returns:
      The gathered Tensor.

    Raises:
      RuntimeError: if called in eager mode.
    """
if context.executing_eagerly():
    raise RuntimeError('all_gather is not supported in eager mode.')

with ops.device(self._device), \
         ops.control_dependencies([array_ops.identity(input_tensor)]):
    # 1. Transpose
    # E.g. Given an input_tensor with shape [2,2,5,1] and axis to gather is 3,
    # we use perm_pre=[3 0 1 2] to reshape it to [1,2,2,5], which
    # brings the 3rd dim first; afterwards we use perm_after=[1,2,3,0] to
    # place it back.
    perm_pre = array_ops.concat(
        ([axis], math_ops.range(axis),
         math_ops.range(axis + 1, array_ops.rank(input_tensor))),
        axis=0)
    input_tensor_t = array_ops.transpose(input_tensor, perm=perm_pre)
    # 2. Pad
    gathered_shape = self._all_gather(
        array_ops.expand_dims_v2(array_ops.shape_v2(input_tensor_t), axis=0),
        options)
    first_dims = gathered_shape[:, 0]
    full_axis_dim = math_ops.reduce_max(first_dims)
    padded_input_tensor = _pad_util(input_tensor_t, full_axis_dim)

    # 3. Gather
    gather_padded_out_tensor = self._all_gather(padded_input_tensor, options)
    # 4. Unpad
    split_tensors = []
    for i in range(self._group_size):
        start_pos = i * full_axis_dim
        split_tensors.append(gather_padded_out_tensor[start_pos:start_pos +
                                                      first_dims[i]])
    out_tensor_t = array_ops.concat(split_tensors, 0)

    # 5. Transpose back
    perm_after = array_ops.concat(
        (math_ops.range(1, axis + 1), [0],
         math_ops.range(axis + 1, array_ops.rank(input_tensor_t))),
        axis=0)
    exit(array_ops.transpose(out_tensor_t, perm=perm_after))
