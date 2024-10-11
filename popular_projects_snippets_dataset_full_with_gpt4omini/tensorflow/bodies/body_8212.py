# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
self._poll_termination_signal_thread_should_stop = threading.Event()
self._poll_termination_signal_thread = threading.Thread(
    target=self._poll_termination_signal,
    name='WorkerTerminationSignalWatcher-%s' % self._id_in_cluster,
    daemon=True)
logging.info('Start polling for termination signal.')
self._poll_termination_signal_thread.start()
