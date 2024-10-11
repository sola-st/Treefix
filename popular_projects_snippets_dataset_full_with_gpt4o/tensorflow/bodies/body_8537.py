# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
"""Create a test session with master target set to the testing cluster.

    Creates a test session that connects to the local testing cluster.
    The session is only created once per test and then reused.

    Args:
      graph: Optional graph to use during the returned session.
      config: An optional config_pb2.ConfigProto to use to configure the
        session.
      target: the target of session to connect to.

    Yields:
      A Session object that should be used as a context manager to surround
      the graph building and execution code in a test case. Note that the
      session will live until the end of the test.
    """
config = self._create_config(config)

if target is None:
    target = self._default_target
if getattr(self._thread_local, 'cached_session', None) is None:
    self._thread_local.cached_session = session.Session(
        graph=None, config=config, target=target)
sess = self._thread_local.cached_session
with sess.graph.as_default(), sess.as_default():
    exit(sess)
