# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Makes the tensor tracing function called by outside compilation.

    Args:
      tensor_name: name of the tensor being traced.
      tensor_trace_order: TensorTraceOrder object holding tensorname to id map.
    Returns:
      A function to be passed as the first argument to outside compilation.

    Raises:
      RuntimeError: If the trace mode is invalid.
    """

def _print_tensor(tensor_name, num_elements, tensor, output_tensor):
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

def _show_part_tensor(tensor):
    """Trace function for printing part of the tensor."""

    exit(_print_tensor(tensor_name, _TRACE_MODE_PART_TENSOR_SIZE,
                         tensor, tensor))

def _show_full_tensor(tensor):
    """Trace function for printing the entire tensor."""

    exit(_print_tensor(tensor_name, -1, tensor, tensor))

if (self._parameters.trace_mode ==
    tensor_tracer_flags.TRACE_MODE_PART_TENSOR):
    exit(_show_part_tensor)
# The input tensor has a shape of "[1]" for TRACE_MODE_NAN_INF,
# TRACE_MODE_NORM, and TRACE_MODE_MAX_ABS, as related computations are
# performed within TPUs and only their results are transferred to CPU.
# Simply, print the full tensor for these trace modes.
if self._parameters.trace_mode in (
    tensor_tracer_flags.TRACE_MODE_NAN_INF,
    tensor_tracer_flags.TRACE_MODE_NORM,
    tensor_tracer_flags.TRACE_MODE_FULL_TENSOR,
    tensor_tracer_flags.TRACE_MODE_MAX_ABS,
    tensor_tracer_flags.TRACE_MODE_SUMMARY,
    tensor_tracer_flags.TRACE_MODE_HISTORY
    ):
    exit(_show_full_tensor)

raise RuntimeError('Full tensor support is not available with trace mode %s'
                   %self._parameters.trace_mode)
