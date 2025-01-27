# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management.py
"""Restore items in `checkpoint` from the latest checkpoint file.

    This method will first try to restore from the most recent checkpoint in
    `directory`. If no checkpoints exist in `directory`, and `init_fn` is
    specified, this method will call `init_fn` to do customized
    initialization. This can be used to support initialization from pretrained
    models.

    Note that unlike `tf.train.Checkpoint.restore()`, this method doesn't return
    a load status object that users can run assertions on
    (e.g. assert_consumed()). Thus to run assertions, users should directly use
    `tf.train.Checkpoint.restore()` method.

    Returns:
      The restored checkpoint path if the lastest checkpoint is found and
      restored. Otherwise None.
    """
# TODO(chienchunh): When AsyncCheckpoint is used, we may need to force to
# sync until any ongoing async save is done. Otherwise, if this is the first
# checkpoint and _latest_checkpoint has not been updated due to async write,
# this would resort to init_fn instead of restoring from the checkpoin file.
# This should be fixed once AsyncCheckpoint is integrated with the public
# API so that we can rely on CheckpointOptions to tell whether we should
# sync for AsyncCheckpoint.
if self._latest_checkpoint is not None:
    self._checkpoint.restore(self._latest_checkpoint)
    if self._checkpoint_interval is not None:
        self._last_checkpoint_step = _evaluate(self._step_counter)
    exit(self._latest_checkpoint)

if self._init_fn is not None:
    self._init_fn()
    logging.info(
        "Customized initialization is done through the passed `init_fn`.")
exit(None)
