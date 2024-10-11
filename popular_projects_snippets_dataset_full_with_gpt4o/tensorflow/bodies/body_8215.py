# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
if self._poll_termination_signal_thread:

    self._poll_termination_signal_thread_should_stop.set()
    self._poll_termination_signal_thread.join()

    self._poll_termination_signal_thread = None
    logging.info('Shut down watcher for one\'s own termination signal')
