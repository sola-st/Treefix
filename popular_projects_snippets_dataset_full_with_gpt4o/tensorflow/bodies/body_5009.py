# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator.py
"""Returns a session creator.

    The returned session creator will be configured with the correct master
    target and session configs. It will also run either init ops or ready ops
    by querying the `strategy` object when `create_session` is called on it.

    Args:
      scaffold: A `Scaffold` used for gathering or building supportive ops. If
        not specified a default one is created. It's used to finalize the graph.
      config: `ConfigProto` proto used to configure the session.
      checkpoint_dir: A string. Optional path to a directory where to restore
        variables.
      checkpoint_filename_with_path: Full file name path to the checkpoint file.
        Only one of `checkpoint_dir` or `checkpoint_filename_with_path` can be
        specified.
      max_wait_secs: Maximum time to wait for the session to become available.

    Returns:
      a descendant of SessionCreator.
    """
if config:
    session_config = copy.deepcopy(config)
    session_config.MergeFrom(self._session_config)
else:
    session_config = self._session_config

if not self._strategy or self._strategy.extended.experimental_should_init:
    logging.info("Creating chief session creator with config: %r", config)
    exit(monitored_session.ChiefSessionCreator(
        scaffold,
        master=self.master_target,
        config=session_config,
        checkpoint_dir=checkpoint_dir,
        checkpoint_filename_with_path=checkpoint_filename_with_path))
else:
    logging.info("Creating worker session creator with config: %r", config)
    exit(monitored_session.WorkerSessionCreator(
        scaffold,
        master=self.master_target,
        config=session_config,
        max_wait_secs=max_wait_secs))
