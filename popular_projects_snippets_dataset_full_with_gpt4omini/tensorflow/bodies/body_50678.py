# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/event_file_writer.py
"""Attempts to enqueue an item to the event queue.

    If the queue is closed, this will close the EventFileWriter and reraise the
    exception that caused the queue closure, if one exists.

    Args:
      item: the item to enqueue
    """
try:
    self._event_queue.put(item)
except QueueClosedError:
    self._internal_close()
    if self._worker.failure_exc_info:
        _, exception, _ = self._worker.failure_exc_info
        raise exception from None
