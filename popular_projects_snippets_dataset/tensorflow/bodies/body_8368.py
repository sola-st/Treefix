# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
"""Batch all-reduce dense tensors.

    This takes a list of batches of tensors. Using multiple batches have the
    benefit that it doesn't need to wait for all inputs to be ready to start the
    all-reduce.

    Args:
      input_tensor_packs: a list of lists of dense tensors.
      options: an optional tf.distribute.experimental.CommunicationOptions. If
        provided, it overrides the default options.

    Returns:
      A flat list of reduced tensors.
    """
options = self._options.merge(options)
outputs = []
for pack in input_tensor_packs:
    if context.executing_eagerly():
        # We don't batch in eager as it sometimes makes the performance worse
        # due the concat/split ops.
        for input_tensor in pack:
            outputs.append(self.all_reduce(input_tensor, None, options))
    else:
        # TODO(b/169168846): inserts a parallel all_gather to verify packings
        # are the same on each replica.
        with ops.device(self._device):
            flat_tensors = [array_ops.reshape(t, [-1]) for t in pack]
            shapes = [array_ops.shape(t) for t in pack]
            if (options.implementation
                == collective_util.CommunicationImplementation.NCCL and outputs):
                control_input = outputs[-1]
            else:
                control_input = None
            reduced = self.all_reduce(
                array_ops.concat(flat_tensors, axis=0), control_input, options)
            num_elements = [math_ops.reduce_prod(s) for s in shapes]
            flat_outputs = array_ops.split(reduced, num_elements, axis=0)
            for shape, flat_output in zip(shapes, flat_outputs):
                outputs.append(array_ops.reshape(flat_output, shape))

exit(outputs)
