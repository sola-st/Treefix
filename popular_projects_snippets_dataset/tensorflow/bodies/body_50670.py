# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/event_file_writer_v2.py
"""Adds an event to the event file.

    Args:
      event: An `Event` protocol buffer.
    """
if not self._closed:
    event_pb = event.SerializeToString()
    self._session.run(
        self._add_event_op, feed_dict={self._event_placeholder: event_pb})
