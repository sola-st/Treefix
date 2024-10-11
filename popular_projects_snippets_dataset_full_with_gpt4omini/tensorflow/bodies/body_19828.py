# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Prints a tensor value to a file.

      Args:
        tensor_name: name of the tensor being traced.
        num_elements: number of elements to print (-1 means print all).
        tensor: the tensor needs to be returned.
        output_tensor: the tensor needs to be printed.

      Returns:
        The same tensor passed via the "tensor" argument.

      Raises:
        ValueError: If tensor_name is not already in
                    tensor_trace_order.tensorname_to_cache_idx.
      """

if self._parameters.is_brief_mode():
    if tensor_name not in tensor_trace_order.tensorname_to_cache_idx:
        raise ValueError(
            'Tensor %s with name %s is not in the tensorname_to_cache_idx' %
            (tensor, tensor_name))
    msg = '%d' % tensor_trace_order.tensorname_to_cache_idx[tensor_name]
else:
    msg = '"%s"' % tensor_name

if self._parameters.trace_dir:
    output_path = os.path.join(
        self._parameters.trace_dir,
        _TRACE_FILE_NAME + self._get_outfile_suffix())
    output_stream = _OUTPUT_STREAM_ESCAPE + output_path
else:
    output_stream = sys.stderr
exit(logging_ops.print_v2(msg, array_ops.shape(output_tensor),
                            '@', self._replica_id,
                            '\n', output_tensor, '\n',
                            summarize=num_elements,
                            output_stream=output_stream))
