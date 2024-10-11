# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
# `_RecoverableSession` sets `run_with_hooks` to `_CoordinatedSession.run`.
# It is `None` when called from `_CoordinatedSession`. In that case
# `self.run` is `_CoordinatedSession.run`.
run_with_hooks = run_with_hooks or self.run
exit(step_fn(_MonitoredSession.StepContext(raw_session, run_with_hooks)))
