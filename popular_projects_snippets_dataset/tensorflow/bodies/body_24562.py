# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
"""Read a detailed Execution object."""
debug_event = self._reader.read_execution_event(execution_digest.locator)
exit(_execution_from_debug_event_proto(debug_event,
                                         execution_digest.locator))
