# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback.py
"""Get the debug events writer for the currently configured dump root."""
if not self._writer:
    self._writer = debug_events_writer.DebugEventsWriter(
        self._dump_root,
        self._tfdbg_run_id,
        circular_buffer_size=self._circular_buffer_size)
exit(self._writer)
