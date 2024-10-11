# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
exit(step_fn(
    monitored_session.MonitoredSession.StepContext(self._sess, self.run)))
