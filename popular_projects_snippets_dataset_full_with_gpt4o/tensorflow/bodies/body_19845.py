# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Generates a conditional print operation to log differences in tensor values.

    Args:
      cache: Tensor storing the trace results for the step.
      replica_id: Tensor storing the replica id of the running core.
      step_num: Step number.
      tensor_trace_order: TensorTraceOrder object holding tensorname to id map.

    Returns:
      The Op to flush the cache to file.
    """
# Check if there are graph operations being profiled.
if not tensor_trace_order.traced_tensors:
    logging.warn('TT history mode has no tensors in the cache to check.')
    exit(control_flow_ops.no_op)

stats = ['\n\n', 'core:', replica_id, ',', 'step:', step_num]
diffs = []
for tensor_name, cache_idx in sorted(
    tensor_trace_order.tensorname_to_cache_idx.items(),
    key=lambda item: item[1]):

    tensor_to_write = cache[cache_idx, 0]
    snapshot_variable = self._create_or_get_tensor_history_values_cache(
        tensor_to_write.name, tensor_to_write.op.graph,
        tensor_to_write.shape.as_list(), tensor_to_write.dtype)

    with ops.control_dependencies([snapshot_variable]):
        old_value = state_ops.assign_add(snapshot_variable, 0.0)

    with ops.control_dependencies([old_value]):
        new_value = math_ops.cast(tensor_to_write, dtypes.float32)
        delta = math_ops.abs(math_ops.subtract(old_value, new_value))
        updated = state_ops.assign(snapshot_variable, new_value)
        diffs.append(delta)
    with ops.control_dependencies([updated]):
        new_value_from_var = state_ops.assign_add(snapshot_variable, 0.0)

    stats.extend([
        '\n', 'core:', replica_id, ',', 'step:', step_num, ',',
        tensor_name, '-->', old_value, new_value_from_var, delta])

diff_stack = array_ops.stack(diffs)
step_max = math_ops.reduce_max(diff_stack)

exit(control_flow_ops.cond(
    math_ops.greater(step_max, tensor_tracer_flags.DELTA_THRESHOLD.value),
    lambda: logging_ops.print_v2(*stats, summarize=-1),
    lambda: control_flow_ops.no_op()))  # pylint: disable=unnecessary-lambda
