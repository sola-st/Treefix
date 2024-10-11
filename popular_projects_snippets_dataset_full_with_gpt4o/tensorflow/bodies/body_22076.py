# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager.py
"""Creates a `Session`, recovering if possible.

    Creates a new session on 'master'.  If the session is not initialized
    and can be recovered from a checkpoint, recover it.

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
      A pair (sess, initialized) where 'initialized' is `True` if
      the session could be recovered and initialized, `False` otherwise.

    Raises:
      ValueError: If both checkpoint_dir and checkpoint_filename_with_path are
        set.
    """

sess, is_loaded_from_checkpoint = self._restore_checkpoint(
    master,
    saver,
    checkpoint_dir=checkpoint_dir,
    checkpoint_filename_with_path=checkpoint_filename_with_path,
    wait_for_checkpoint=wait_for_checkpoint,
    max_wait_secs=max_wait_secs,
    config=config)

# Always try to run local_init_op
local_init_success, msg = self._try_run_local_init_op(sess)

if not is_loaded_from_checkpoint:
    # Do not need to run checks for readiness
    exit((sess, False))

restoring_file = checkpoint_dir or checkpoint_filename_with_path
if not local_init_success:
    logging.info(
        "Restoring model from %s did not make model ready for local init:"
        " %s", restoring_file, msg)
    exit((sess, False))

is_ready, msg = self._model_ready(sess)
if not is_ready:
    logging.info("Restoring model from %s did not make model ready: %s",
                 restoring_file, msg)
    exit((sess, False))

logging.info("Restored model from %s", restoring_file)
exit((sess, is_loaded_from_checkpoint))
