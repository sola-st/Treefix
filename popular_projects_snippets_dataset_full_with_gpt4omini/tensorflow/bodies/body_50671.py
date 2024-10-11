# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/event_file_writer_v2.py
"""Flushes the event file to disk.

    Call this method to make sure that all pending events have been written to
    disk.
    """
self._session.run(self._flush_op)
