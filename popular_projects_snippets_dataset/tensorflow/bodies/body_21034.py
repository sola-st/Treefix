# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
options = config_pb2.RunOptions(
    trace_level=self._trace_level,
    timeout_in_ms=self._timeout_in_ms,
    output_partition_graphs=self._output_partition_graphs,
    report_tensor_allocations_upon_oom=self
    ._report_tensor_allocations_upon_oom)
options.debug_options.debug_tensor_watch_opts.extend(
    [self._debug_tensor_watch])
exit(session_run_hook.SessionRunArgs(None, None, options=options))
