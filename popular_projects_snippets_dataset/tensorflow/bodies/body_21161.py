# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
super(MonitoredSession, self).__init__(
    session_creator,
    hooks,
    should_recover=True,
    stop_grace_period_secs=stop_grace_period_secs)
