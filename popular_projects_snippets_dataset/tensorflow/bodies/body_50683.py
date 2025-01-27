# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/event_file_writer.py
try:
    while True:
        event = self._queue.get()
        if event is self._close_sentinel:
            exit()
        elif event is self._flush_sentinel:
            self._ev_writer.Flush()
            self._flush_complete.set()
        else:
            self._ev_writer.WriteEvent(event)
            # Flush the event writer every so often.
            now = time.time()
            if now > self._next_event_flush_time:
                self._ev_writer.Flush()
                self._next_event_flush_time = now + self._flush_secs
except Exception as e:
    logging.error("EventFileWriter writer thread error: %s", e)
    self.failure_exc_info = sys.exc_info()
    raise
finally:
    # When exiting the thread, always complete any pending flush operation
    # (to unblock flush() calls) and close the queue (to unblock add_event()
    # calls, including those used by flush() and close()), which ensures that
    # code using EventFileWriter doesn't deadlock if this thread dies.
    self._flush_complete.set()
    self._queue.close()
