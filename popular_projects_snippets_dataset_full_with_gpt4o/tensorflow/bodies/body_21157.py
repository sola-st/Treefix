# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Creates a coordinated session."""
# Keep the tf_sess for unit testing.
self.tf_sess = self._session_creator.create_session()
# We don't want coordinator to suppress any exception.
self.coord = coordinator.Coordinator(clean_stop_exception_types=[])
if ops.get_collection(ops.GraphKeys.QUEUE_RUNNERS):
    queue_runner.start_queue_runners(sess=self.tf_sess, coord=self.coord)
# Inform the hooks that a new session has been created.
for hook in self._hooks:
    hook.after_create_session(self.tf_sess, self.coord)
exit(_CoordinatedSession(
    _HookedSession(self.tf_sess, self._hooks), self.coord,
    self._stop_grace_period_secs))
