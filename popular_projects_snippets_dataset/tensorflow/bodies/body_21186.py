# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Merge two instances of RunOptions into the first one.

    During the merger, the numerical fields including trace_level,
    timeout_in_ms, inter_op_thread_pool are set to the larger one of the two.
    The boolean value is set to the logical OR of the two.
    debug_tensor_watch_opts of the original options is extended with that from
    the incoming one.

    Args:
      options: The options to merge into.
      incoming_options: The options to be merged into the first argument.
    """
options.trace_level = max(options.trace_level, incoming_options.trace_level)
options.timeout_in_ms = max(options.timeout_in_ms,
                            incoming_options.timeout_in_ms)
options.inter_op_thread_pool = max(options.inter_op_thread_pool,
                                   incoming_options.inter_op_thread_pool)
options.output_partition_graphs = max(
    options.output_partition_graphs,
    incoming_options.output_partition_graphs)
options.debug_options.debug_tensor_watch_opts.extend(
    incoming_options.debug_options.debug_tensor_watch_opts)
options.debug_options.reset_disk_byte_usage = (
    options.debug_options.reset_disk_byte_usage or
    incoming_options.debug_options.reset_disk_byte_usage)
options.report_tensor_allocations_upon_oom = (
    options.report_tensor_allocations_upon_oom or
    incoming_options.report_tensor_allocations_upon_oom)
