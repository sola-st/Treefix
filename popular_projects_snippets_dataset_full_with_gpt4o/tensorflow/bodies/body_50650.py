# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer.py
"""Adds an event to the event file.

    Args:
      event: An `Event` protocol buffer.
    """
self._warn_if_event_writer_is_closed()
self.event_writer.add_event(event)
