# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Initializes a worker session creator.

    Args:
      scaffold: A `Scaffold` used for gathering or building supportive ops. If
        not specified a default one is created. It's used to finalize the graph.
      master: `String` representation of the TensorFlow master to use.
      config: `ConfigProto` proto used to configure the session.
      max_wait_secs: Maximum time to wait for the session to become available.
    """
self._scaffold = scaffold or Scaffold()
self._session_manager = None
self._master = master
self._config = config
self._max_wait_secs = max_wait_secs
