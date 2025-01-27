# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Initializes a chief session creator.

    Args:
      scaffold: A `Scaffold` used for gathering or building supportive ops. If
        not specified a default one is created. It's used to finalize the graph.
      master: `String` representation of the TensorFlow master to use.
      config: `ConfigProto` proto used to configure the session.
      checkpoint_dir: A string.  Optional path to a directory where to restore
        variables.
      checkpoint_filename_with_path: Full file name path to the checkpoint file.
    """
self._checkpoint_dir = checkpoint_dir
self._checkpoint_filename_with_path = checkpoint_filename_with_path
self._scaffold = scaffold or Scaffold()
self._session_manager = None
self._master = master
self._config = config
