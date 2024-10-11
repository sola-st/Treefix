# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/event_file_writer.py
"""Creates an _EventLoggerThread.

    Args:
      queue: A CloseableQueue from which to dequeue events. The queue will be
        closed just before the thread exits, whether due to `close_sentinel` or
        any exception raised in the writing loop.
      ev_writer: An event writer. Used to log brain events for
        the visualizer.
      flush_secs: How often, in seconds, to flush the
        pending file to disk.
      flush_complete: A threading.Event that will be set whenever a flush
        operation requested via `flush_sentinel` has been completed.
      flush_sentinel: A sentinel element in queue that tells this thread to
        flush the writer and mark the current flush operation complete.
      close_sentinel: A sentinel element in queue that tells this thread to
        terminate and close the queue.
    """
threading.Thread.__init__(self, name="EventLoggerThread")
self.daemon = True
self._queue = queue
self._ev_writer = ev_writer
self._flush_secs = flush_secs
# The first event will be flushed immediately.
self._next_event_flush_time = 0
self._flush_complete = flush_complete
self._flush_sentinel = flush_sentinel
self._close_sentinel = close_sentinel
# Populated when writing logic raises an exception and kills the thread.
self.failure_exc_info = ()
