# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/event_file_writer.py
"""Initializes or re-initializes the queue and writer thread.

    The EventsWriter itself does not need to be re-initialized explicitly,
    because it will auto-initialize itself if used after being closed.
    """
self._event_queue = CloseableQueue(self._max_queue)
self._worker = _EventLoggerThread(self._event_queue, self._ev_writer,
                                  self._flush_secs, self._flush_complete,
                                  self._flush_sentinel,
                                  self._close_sentinel)

self._worker.start()
