# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
self._session_creator = session_creator
self._hooks = hooks
self.coord = None
self.tf_sess = None
self._stop_grace_period_secs = stop_grace_period_secs
