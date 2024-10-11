# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
last_step = session.run(self._global_step_tensor)
if last_step != self._timer.last_triggered_step():
    self._save(session, last_step)
for l in self._listeners:
    l.end(session, last_step)
