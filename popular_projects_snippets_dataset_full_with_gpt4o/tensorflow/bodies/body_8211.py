# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
logging.info('Start watcher for local signal.')
signal.signal(signal.SIGTERM, self._sigterm_handler_fn)
