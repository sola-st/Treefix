# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/event_file_writer.py
"""Put an item into the queue.

    If the queue is closed, fails immediately.

    If the queue is full, blocks until space is available or until the queue
    is closed by a call to close(), at which point this call fails.

    Args:
      item: an item to add to the queue

    Raises:
      QueueClosedError: if insertion failed because the queue is closed
    """
with self._not_full:
    if self._closed:
        raise QueueClosedError()
    if self._maxsize > 0:
        while len(self._queue) == self._maxsize:
            self._not_full.wait()
            if self._closed:
                raise QueueClosedError()
    self._queue.append(item)
    self._not_empty.notify()
