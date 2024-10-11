# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
logging.info('Stopping worker watchdog.')
self._reset_manager(stopping=True)
self._running = False
self.join()
