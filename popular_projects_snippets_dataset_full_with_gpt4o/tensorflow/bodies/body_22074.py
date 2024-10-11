# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager.py
"""Creates a `Session`, and tries to restore a checkpoint.


    Args:
      master: `String` representation of the TensorFlow master to use.
      saver: A `Saver` object used to restore a model.
      checkpoint_dir: Path to the checkpoint files. The latest checkpoint in the
        dir will be used to restore.
      checkpoint_filename_with_path: Full file name path to the checkpoint file.
      wait_for_checkpoint: Whether to wait for checkpoint to become available.
      max_wait_secs: Maximum time to wait for checkpoints to become available.
      config: Optional `ConfigProto` proto used to configure the session.

    Returns:
      A pair (sess, is_restored) where 'is_restored' is `True` if
      the session could be restored, `False` otherwise.

    Raises:
      ValueError: If both checkpoint_dir and checkpoint_filename_with_path are
        set.
    """
self._target = master

# This is required to so that we initialize the TPU device before
# restoring from checkpoint since we'll be placing variables on the device
# and TPUInitialize wipes out the memory of the device.
strategy = distribution_strategy_context.get_strategy()
if strategy and hasattr(strategy.extended,
                        "_experimental_initialize_system"):
    strategy.extended._experimental_initialize_system()  # pylint: disable=protected-access

sess = session.Session(self._target, graph=self._graph, config=config)
if checkpoint_dir and checkpoint_filename_with_path:
    raise ValueError("Can not provide both checkpoint_dir and "
                     "checkpoint_filename_with_path.")
# If either saver or checkpoint_* is not specified, cannot restore. Just
# return.
if not saver or not (checkpoint_dir or checkpoint_filename_with_path):
    exit((sess, False))

if checkpoint_filename_with_path:
    _restore_checkpoint_and_maybe_run_saved_model_initializers(
        sess, saver, checkpoint_filename_with_path)
    exit((sess, True))

# Waits up until max_wait_secs for checkpoint to become available.
wait_time = 0
ckpt = checkpoint_management.get_checkpoint_state(checkpoint_dir)
while not ckpt or not ckpt.model_checkpoint_path:
    if wait_for_checkpoint and wait_time < max_wait_secs:
        logging.info("Waiting for checkpoint to be available.")
        time.sleep(self._recovery_wait_secs)
        wait_time += self._recovery_wait_secs
        ckpt = checkpoint_management.get_checkpoint_state(checkpoint_dir)
    else:
        exit((sess, False))

    # Loads the checkpoint.
_restore_checkpoint_and_maybe_run_saved_model_initializers(
    sess, saver, ckpt.model_checkpoint_path)
saver.recover_last_checkpoints(ckpt.all_model_checkpoint_paths)
exit((sess, True))
