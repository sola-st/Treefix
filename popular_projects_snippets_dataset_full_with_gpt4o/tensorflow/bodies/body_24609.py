# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_monitors_test.py
if graph_execution_trace_index in self.graph_execution_traces:
    raise ValueError("Duplicate graph-execution-trace index: %d" %
                     graph_execution_trace_index)
self.graph_execution_traces[
    graph_execution_trace_index] = graph_execution_trace
