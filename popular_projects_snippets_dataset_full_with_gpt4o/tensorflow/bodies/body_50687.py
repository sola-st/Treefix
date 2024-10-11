# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/event_file_writer.py
"""Closes the queue, causing any pending or future `put()` calls to fail."""
with self._not_full:
    self._closed = True
    self._not_full.notify_all()
