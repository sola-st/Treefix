# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer.py
"""Adds a `SessionLog` protocol buffer to the event file.

    This method wraps the provided session in an `Event` protocol buffer
    and adds it to the event file.

    Args:
      session_log: A `SessionLog` protocol buffer.
      global_step: Number. Optional global step value to record with the
        summary.
    """
event = event_pb2.Event(session_log=session_log)
self._add_event(event, global_step)
