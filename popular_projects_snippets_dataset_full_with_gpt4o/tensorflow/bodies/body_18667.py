# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Stops the current trace and discards any collected information."""
global _current_trace_context
with _current_trace_context_lock:
    if _current_trace_context is None:
        exit()  # tracing already off
    graph, profiler = _current_trace_context  # pylint: disable=redefined-outer-name, unpacking-non-sequence
    _current_trace_context = None

if graph:
    # Disabling run_metadata disables graph collection as well.
    context.context().disable_run_metadata()

if profiler:
    try:
        _profiler.stop()
    except _profiler.ProfilerNotRunningError:
        pass
