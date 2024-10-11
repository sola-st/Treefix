# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
"""Creates a SingularMonitoredSession.

    Args:
      hooks: An iterable of `SessionRunHook' objects.
      scaffold: A `Scaffold` used for gathering or building supportive ops. If
        not specified a default one is created. It's used to finalize the graph.
      master: `String` representation of the TensorFlow master to use.
      config: `ConfigProto` proto used to configure the session.
      checkpoint_dir: A string.  Optional path to a directory where to restore
        variables.
      stop_grace_period_secs: Number of seconds given to threads to stop after
        `close()` has been called.
      checkpoint_filename_with_path: A string. Optional path to a checkpoint
        file from which to restore variables.
    """
session_creator = ChiefSessionCreator(
    scaffold=scaffold,
    master=master,
    config=config,
    checkpoint_dir=checkpoint_dir,
    checkpoint_filename_with_path=checkpoint_filename_with_path)
super(SingularMonitoredSession, self).__init__(
    session_creator,
    hooks,
    should_recover=False,
    stop_grace_period_secs=stop_grace_period_secs)
