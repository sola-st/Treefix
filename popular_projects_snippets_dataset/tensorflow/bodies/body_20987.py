# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
self._coord = coord
exit(StopCoordinatorWithException.after_create_session(
    self, session, coord))
