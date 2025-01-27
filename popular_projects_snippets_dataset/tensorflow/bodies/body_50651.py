# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer.py
"""Flushes the event file to disk.

    Call this method to make sure that all pending events have been written to
    disk.
    """
# Flushing a closed EventFileWriterV2 raises an exception. It is,
# however, a noop for EventFileWriter.
self._warn_if_event_writer_is_closed()
self.event_writer.flush()
