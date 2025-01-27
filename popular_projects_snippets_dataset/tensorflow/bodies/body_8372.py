# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
"""All-reduce an IndexedSlices.

    This method must be called inside a tf.function.

    Args:
      input_slices: an IndexedSlices.
      options: an optional tf.distribute.experimental.CommunicationOptions. If
        provided, it overrides the default options.

    Returns:
      The reduced IndexedSlices.

    Raises:
      RuntimeError: if called in eager mode.
    """
if context.executing_eagerly():
    raise RuntimeError(
        'all_reduce_indexed_slices is not supported in eager mode.')

# Current CollectiveAllGather implementations require input IndexedSlices to
# have consistent length across the board, we handle the reduction of
# IndexedSlices as follows:
#   1. Gather the lengths of IndexedSlices from all participants.
#   2. If they have consistent length, apply all_gather.
#   3. Otherwise pad IndexedSlices to be the same length across all
#      participants and apply_gather.
options = self._options.merge(options)
with ops.device(self._device):

    def all_gather_indexed_slices(
        all_gather_fn: Callable[
            [core.TensorLike, Optional[collective_util.Options]], core.Tensor]
    ) -> indexed_slices.IndexedSlices:
        """Use all_gather_fn to aggregate `IndexedSlices`."""
        all_values = all_gather_fn(input_slices.values, options)
        # Add control dependency to order the all-gather.
        if (options.implementation ==
            collective_util.CommunicationImplementation.NCCL):
            control = [all_values]
        else:
            control = []
        with ops.control_dependencies(control):
            all_indices = all_gather_fn(input_slices.indices, options)
        exit(indexed_slices.IndexedSlices(
            values=all_values,
            indices=all_indices,
            dense_shape=input_slices.dense_shape))

    length = array_ops.shape(input_slices.indices)
    all_lengths = self._all_gather(length, options)

    def all_gather_with_padding(
        input_tensor: core.TensorLike,
        options: Optional[collective_util.Options]) -> core.Tensor:
        """all_gather tensors of different sizes using padding."""
        max_length = math_ops.reduce_max(all_lengths)
        padded_tensor = _pad_util(input_tensor, max_length)
        all_padded_tensors = self._all_gather(padded_tensor, options)
        split_tensors = []
        for i in range(self._group_size):
            start_pos = i * max_length
            split_tensors.append(all_padded_tensors[start_pos:start_pos +
                                                    all_lengths[i]])
        exit(array_ops.concat(split_tensors, 0))

    exit(control_flow_ops.cond(
        math_ops.equal(
            math_ops.reduce_max(all_lengths),
            math_ops.reduce_min(all_lengths)),
        lambda: all_gather_indexed_slices(self._all_gather),
        lambda: all_gather_indexed_slices(all_gather_with_padding)))
