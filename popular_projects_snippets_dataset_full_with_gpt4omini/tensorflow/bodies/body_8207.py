# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling.py
"""Creates the `PreemptionCheckpointHandler`.

    Args:
      cluster_resolver: a `tf.distribute.cluster_resolver.ClusterResolver`
        object. You may also obtain it through the `cluster_resolver` attribute
        of the distribution strategy in use.
      checkpoint_or_checkpoint_manager: a `tf.train.CheckpointManager` or a
        `tf.train.Checkpoint`. If you are using a `tf.train.CheckpointManager`
        to manage checkpoints outside the `PreemptionCheckpointHandler` for
        backup purpose as well, pass it as `checkpoint_or_checkpoint_manager`
        argument. Otherwise, pass a `tf.train.Checkpoint` and the
        `PreemptionCheckpointHandler` will create
        a `tf.train.CheckpointManager` to manage it in the `checkpoint_dir`.
      checkpoint_dir: a directory where the `PreemptionCheckpointHandler` saves
        and restores checkpoints. When a `PreemptionCheckpointHandler` is
        created, the latest checkpoint in the `checkpoint_dir` will be restored.
        (This is not needed if a `tf.train.CheckpointManager` instead of a
        `tf.train.Checkpoint` is passed as the
        `checkpoint_or_checkpoint_manager` argument.)
      termination_config: optional, a
        `tf.distribute.experimental.TerminationConfig` object to configure for a
        platform other than Google Borg or GCP.
    """
# TODO(wxinyi): Maybe make checkpoint_or_checkpoint_manager optional if
# save_fn is passed. For now it's still useful for restore.
if isinstance(checkpoint_or_checkpoint_manager,
              checkpoint_lib.Checkpoint) and not checkpoint_dir:
    raise errors.InvalidArgumentError('When a checkpoint is passed, a '
                                      'checkpoint_dir must be passed as well'
                                      '.')

self._cluster_resolver = cluster_resolver
self._termination_config = termination_config
self._checkpoint_or_checkpoint_manager = checkpoint_or_checkpoint_manager
self._checkpoint_dir = checkpoint_dir

self._platform_device = failure_handling_util.detect_platform()

completed_termination_config = _complete_config_for_environment(
    self._platform_device, self._termination_config)
self._termination_watcher_fn = completed_termination_config.termination_watcher_fn
self._exit_fn = completed_termination_config.exit_fn
self._grace_period = completed_termination_config.grace_period
self._save_fn = completed_termination_config.save_fn

if self._platform_device in (failure_handling_util.PlatformDevice.GCE_TPU,
                             failure_handling_util.PlatformDevice.GCE_CPU):
    # While running MultiWorkerMirroredStrategy training with GPUs and CPUs
    # are the same on Borg, GCE CPU VM and GPU VM are different in terms
    # of live migration, grace period, etc. We can make it work upon request.
    raise NotImplementedError('PreemptionCheckpointHandler does not support '
                              'usage with TPU or CPU device on GCP.')

elif self._platform_device == failure_handling_util.PlatformDevice.INTERNAL_TPU:
    self._initialize_for_tpu_strategy()

else:
    self._initialize_for_multi_worker_mirrored()

logging.info('PreemptionCheckpointHandler initialized or restored.')
