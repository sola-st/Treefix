# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
"""Return MonitoredSession that triggers coordinator failures."""
session = monitored_session.MonitoredSession(session_creator, [hook])
# We would like to test a situation where during fetches through the
# raw session, the coordinator fails with an exception.  To do that, we
# are going to use (raw_session + StopCoordinatorWithException) hook
# combination that is stored in
# `MonitoredSession._RecoverableSession._CoordinatedSession._sess`
# at this point:
session._tf_sess = lambda: session._sess._sess._sess
# `run()` on such a session is equivalent to `run()` on the raw session
# with separate coordinator threads independently stopping with an
# exception.
exit(session)
