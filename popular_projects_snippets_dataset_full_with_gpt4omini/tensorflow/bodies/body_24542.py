# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Incrementally load the .graph_execution_traces file."""
for i, traces_iter in enumerate(
    self._reader.graph_execution_traces_iterators()):
    for debug_event, offset in traces_iter:
        self._graph_execution_trace_digests.append(
            self._graph_execution_trace_digest_from_debug_event_proto(
                debug_event, (i, offset)))
        if self._monitors:
            graph_execution_trace = (
                self._graph_execution_trace_from_debug_event_proto(
                    debug_event, (i, offset)))
            for monitor in self._monitors:
                monitor.on_graph_execution_trace(
                    len(self._graph_execution_trace_digests) - 1,
                    graph_execution_trace)
