# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/event_file_writer.py
"""Flushes the event file to disk.

    Call this method to make sure that all pending events have been written to
    disk.
    """
if not self._closed:
    # Request a flush operation by enqueing a sentinel and then waiting for
    # the writer thread to mark the flush as complete.
    self._flush_complete.clear()
    self._try_put(self._flush_sentinel)
    self._flush_complete.wait()
    if self._worker.failure_exc_info:
        self._internal_close()
        _, exception, _ = self._worker.failure_exc_info
        raise exception
