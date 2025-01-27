# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
"""Create a test session with master target set to the testing cluster.

    Creates a test session that connects to the local testing cluster.

    Args:
      graph: Optional graph to use during the returned session.
      config: An optional config_pb2.ConfigProto to use to configure the
        session.
      target: the target of session to connect to.

    Yields:
      A Session object that should be used as a context manager to surround
      the graph building and execution code in a test case.
    """
config = self._create_config(config)

if target is None:
    target = self._default_target
with session.Session(graph=graph, config=config, target=target) as sess:
    exit(sess)
