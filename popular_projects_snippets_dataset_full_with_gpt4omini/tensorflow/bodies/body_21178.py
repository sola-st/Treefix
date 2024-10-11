# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
# If the coordinator was asked to stop due to an exception, then it needs
# to be propagated to this stack.
self._coord.raise_requested_exception()
# At this point, no exceptions are recorded in the coordinator.
exit(self._coord.should_stop())
