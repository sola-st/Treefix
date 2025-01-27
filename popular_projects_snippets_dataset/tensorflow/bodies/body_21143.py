# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
self._scaffold.finalize()
exit(self._get_session_manager().wait_for_session(
    self._master, config=self._config, max_wait_secs=self._max_wait_secs))
