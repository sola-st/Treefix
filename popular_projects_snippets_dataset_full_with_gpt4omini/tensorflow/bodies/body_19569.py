# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
logging.info(
    'Enabling watchdog timer with %d second timeout '
    'and %d second ping interval.', self.shutdown_timeout,
    self.ping_interval)
self._reset_manager()
self._running = True
self.start()
