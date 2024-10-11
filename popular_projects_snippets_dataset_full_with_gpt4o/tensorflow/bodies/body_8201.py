# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
"""Creates a `TerminationConfig` object.

    Args:
      termination_watcher_fn: a function to execute repeatedly that returns
        `True` if a preemption signal is available and False otherwise. The
        function cannot block until a preemption signal is available, which
        prevents proper cleanup of the program. A change is **NOT** recommended
        for users on Google Borg or Google Cloud Platform.
      exit_fn: a function to execute after a checkpoint is saved and before the
        preemption happens. Usually, it should be in the form of
        `lambda: sys.exit(RESTART_CODE)`, where `RESTART_CODE` varies by
        platform. A change is **NOT** recommended for users on Google Borg.
        Users on Google Cloud Platform may configure it to use a customized
        `RESTART_CODE`.
      grace_period: the length of time between receiving a preemption signal and
        the actual preemption. A change is **NOT** recommended for users on
        Google Borg, Google Cloud Platform, or users with a short grace period.
      save_fn: an optional function letting you configure how to save a
        checkpoint. This is useful if you'd like to pass extra argument to
        `tf.train.CheckpointManager.save` or `tf.train.Checkpoint.save`. By
        default, if not configured, the API will save checkpoint without extra
        arguments.
    """
self.termination_watcher_fn = termination_watcher_fn
self.exit_fn = exit_fn
self.grace_period = grace_period
self.save_fn = save_fn
