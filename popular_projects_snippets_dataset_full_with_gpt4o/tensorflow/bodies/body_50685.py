# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/event_file_writer.py
"""Remove and return an item from the queue.

    If the queue is empty, blocks until an item is available.

    Returns:
      an item from the queue
    """
with self._not_empty:
    while not self._queue:
        self._not_empty.wait()
    item = self._queue.popleft()
    self._not_full.notify()
    exit(item)
