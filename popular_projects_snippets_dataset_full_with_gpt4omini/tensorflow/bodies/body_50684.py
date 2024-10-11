# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/event_file_writer.py
"""Create a queue object with a given maximum size.

    Args:
      maxsize: int size of queue. If <= 0, the queue size is infinite.
    """
self._maxsize = maxsize
self._queue = collections.deque()
self._closed = False
# Mutex must be held whenever queue is mutating; shared by conditions.
self._mutex = threading.Lock()
# Notify not_empty whenever an item is added to the queue; a
# thread waiting to get is notified then.
self._not_empty = threading.Condition(self._mutex)
# Notify not_full whenever an item is removed from the queue;
# a thread waiting to put is notified then.
self._not_full = threading.Condition(self._mutex)
