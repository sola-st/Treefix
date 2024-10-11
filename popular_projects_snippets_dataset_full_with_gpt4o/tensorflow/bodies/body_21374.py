# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Restores previously saved variables.

    This method runs the ops added by the constructor for restoring variables.
    It requires a session in which the graph was launched.  The variables to
    restore do not have to have been initialized, as restoring is itself a way
    to initialize variables.

    The `save_path` argument is typically a value previously returned from a
    `save()` call, or a call to `latest_checkpoint()`.

    Args:
      sess: A `Session` to use to restore the parameters. None in eager mode.
      save_path: Path where parameters were previously saved.

    Raises:
      ValueError: If save_path is None or not a valid checkpoint.
    """
start_time = time.time()
if self._is_empty:
    exit()
if save_path is None:
    raise ValueError("Can't load save_path when it is None.")

checkpoint_prefix = compat.as_text(save_path)
if not checkpoint_management.checkpoint_exists_internal(checkpoint_prefix):
    raise ValueError("The passed save_path is not a valid checkpoint: " +
                     checkpoint_prefix)

logging.info("Restoring parameters from %s", checkpoint_prefix)
try:
    if context.executing_eagerly():
        self._build_eager(save_path, build_save=False, build_restore=True)
    else:
        sess.run(self.saver_def.restore_op_name,
                 {self.saver_def.filename_tensor_name: save_path})
except errors.NotFoundError as err:
    # There are three common conditions that might cause this error:
    # 0. The file is missing. We ignore here, as this is checked above.
    # 1. This is an object-based checkpoint trying name-based loading.
    # 2. The graph has been altered and a variable or other name is missing.

    # 1. The checkpoint would not be loaded successfully as is. Try to parse
    # it as an object-based checkpoint.
    try:
        names_to_keys = object_graph_key_mapping(save_path)
    except errors.NotFoundError:
        # 2. This is not an object-based checkpoint, which likely means there
        # is a graph mismatch. Re-raise the original error with
        # a helpful message (b/110263146)
        raise _wrap_restore_error_with_msg(
            err, "a Variable name or other graph key that is missing")

    # This is an object-based checkpoint. We'll print a warning and then do
    # the restore.
    logging.warning(
        "Restoring an object-based checkpoint using a name-based saver. This "
        "may be somewhat fragile, and will re-build the Saver. Instead, "
        "consider loading object-based checkpoints using "
        "tf.train.Checkpoint().")
    self._object_restore_saver = saver_from_object_based_checkpoint(
        checkpoint_path=save_path,
        var_list=self._var_list,
        builder=self._builder,
        names_to_keys=names_to_keys,
        cached_saver=self._object_restore_saver)
    self._object_restore_saver.restore(sess=sess, save_path=save_path)
except errors.InvalidArgumentError as err:
    # There is a mismatch between the graph and the checkpoint being loaded.
    # We add a more reasonable error message here to help users (b/110263146)
    raise _wrap_restore_error_with_msg(
        err, "a mismatch between the current graph and the graph")
metrics.AddCheckpointReadDuration(
    api_label=_SAVER_LABEL,
    microseconds=_get_duration_microseconds(start_time, time.time()))
