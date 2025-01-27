# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/event_file_writer.py
"""Adds an event to the event file.

    Args:
      event: An `Event` protocol buffer.
    """
if not self._closed:
    self._try_put(event)
