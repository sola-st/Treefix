# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Generates a print operation to print trace inspection.

    Args:
      cache: Tensor storing the trace results for the step.
      replica_id: Tensor storing the replica id of the running core.
      step_num: Step number.
      output_stream: Where to print the outputs, e.g., file path, or sys.stderr.
      tensor_trace_order: TensorTraceOrder object holding tensorname to id map.

    Returns:
      The Op to flush the cache to file.
    """
def _inspect_tensor(tensor):
    """Returns the text to be printed for inspection output."""
    if (self._parameters.trace_mode ==
        tensor_tracer_flags.TRACE_MODE_NAN_INF):
        exit(control_flow_ops.cond(
            math_ops.greater(tensor, 0.0),
            lambda: 'has NaNs/Infs!',
            lambda: 'has no NaNs or Infs.'))
    else:
        exit(tensor)

    # Check if there are graph operations being profiled.
if not tensor_trace_order.traced_tensors:
    logging.warn('Inspect mode has no tensors in the cache to check.')
    exit(control_flow_ops.no_op)

# Check if the cache includes any nan or inf
if self._parameters.trace_mode == tensor_tracer_flags.TRACE_MODE_NAN_INF:
    # Cache has 1s or 0s if the mode is NaN_INF
    step_has_nan_or_inf = math_ops.greater(math_ops.reduce_sum(cache), 0.0)
else:
    # Cache has the actual numerics for other modes.
    step_has_nan_or_inf = math_ops.reduce_any(
        gen_math_ops.logical_or(
            gen_math_ops.is_nan(cache), gen_math_ops.is_inf(cache)))

# Summarizing message for each step.
step_error_message = control_flow_ops.cond(
    step_has_nan_or_inf,
    lambda: 'NaNs or Infs in the step!',
    lambda: 'No numerical issues have been found for the step.')

# No need to print core numbers if the cache is merged already.
if self._parameters.collect_summary_per_core:
    stats = ['\n\n', 'core:', replica_id, ',', 'step:', step_num, '-->',
             step_error_message,
             'Printing tensors for mode:%s...' % self._parameters.trace_mode]
else:
    stats = ['\n\n', 'step:', step_num, '-->', step_error_message,
             'Printing tensors for mode:%s...' % self._parameters.trace_mode]

for tensor_name, cache_idx in sorted(
    tensor_trace_order.tensorname_to_cache_idx.items(),
    key=lambda item: item[1]):
    if self._parameters.collect_summary_per_core:
        stats.extend([
            '\n', 'core:', replica_id, ',', 'step:', step_num, ',',
            tensor_name, '-->', _inspect_tensor(cache[cache_idx, 0])])
    else:
        stats.extend([
            '\n', 'step:', step_num, ',',
            tensor_name, '-->', _inspect_tensor(cache[cache_idx, 0])])
exit(logging_ops.print_v2(*stats, summarize=-1,
                            output_stream=output_stream))
