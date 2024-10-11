# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Incrementally read the .execution file."""
execution_iter = self._reader.execution_iterator()
for debug_event, offset in execution_iter:
    self._execution_digests.append(
        _execution_digest_from_debug_event_proto(debug_event, offset))
    if self._monitors:
        execution = _execution_from_debug_event_proto(debug_event, offset)
        for monitor in self._monitors:
            monitor.on_execution(len(self._execution_digests) - 1, execution)
