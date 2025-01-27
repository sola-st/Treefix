# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Creates a `Saver`.

    The constructor adds ops to save and restore variables.

    `var_list` specifies the variables that will be saved and restored. It can
    be passed as a `dict` or a list:

    * A `dict` of names to variables: The keys are the names that will be
      used to save or restore the variables in the checkpoint files.
    * A list of variables: The variables will be keyed with their op name in
      the checkpoint files.

    For example:

    ```python
    v1 = tf.Variable(..., name='v1')
    v2 = tf.Variable(..., name='v2')

    # Pass the variables as a dict:
    saver = tf.compat.v1.train.Saver({'v1': v1, 'v2': v2})

    # Or pass them as a list.
    saver = tf.compat.v1.train.Saver([v1, v2])
    # Passing a list is equivalent to passing a dict with the variable op names
    # as keys:
    saver = tf.compat.v1.train.Saver({v.op.name: v for v in [v1, v2]})
    ```

    Note: the newer `AutoTrackable` API is not supported by `Saver`. In this
    case, the `tf.train.Checkpoint` class should be used.

    The optional `reshape` argument, if `True`, allows restoring a variable from
    a save file where the variable had a different shape, but the same number
    of elements and type.  This is useful if you have reshaped a variable and
    want to reload it from an older checkpoint.

    The optional `sharded` argument, if `True`, instructs the saver to shard
    checkpoints per device.

    Args:
      var_list: A list of `Variable`/`SaveableObject`, or a dictionary mapping
        names to `SaveableObject`s. If `None`, defaults to the list of all
        saveable objects.
      reshape: If `True`, allows restoring parameters from a checkpoint where
        the variables have a different shape.
      sharded: If `True`, shard the checkpoints, one per device.
      max_to_keep: Maximum number of recent checkpoints to keep. Defaults to 5.
      keep_checkpoint_every_n_hours: How often to keep checkpoints. Defaults to
        10,000 hours.
      name: String.  Optional name to use as a prefix when adding operations.
      restore_sequentially: A `Bool`, which if true, causes restore of different
        variables to happen sequentially within each device.  This can lower
        memory usage when restoring very large models.
      saver_def: Optional `SaverDef` proto to use instead of running the
        builder. This is only useful for specialty code that wants to recreate a
        `Saver` object for a previously built `Graph` that had a `Saver`. The
        `saver_def` proto should be the one returned by the `as_saver_def()`
        call of the `Saver` that was created for that `Graph`.
      builder: Optional `SaverBuilder` to use if a `saver_def` was not provided.
        Defaults to `BulkSaverBuilder()`.
      defer_build: If `True`, defer adding the save and restore ops to the
        `build()` call. In that case `build()` should be called before
        finalizing the graph or using the saver.
      allow_empty: If `False` (default) raise an error if there are no variables
        in the graph. Otherwise, construct the saver anyway and make it a no-op.
      write_version: controls what format to use when saving checkpoints.  It
        also affects certain filepath matching logic.  The V2 format is the
        recommended choice: it is much more optimized than V1 in terms of memory
        required and latency incurred during restore.  Regardless of this flag,
        the Saver is able to restore from both V2 and V1 checkpoints.
      pad_step_number: if True, pads the global step number in the checkpoint
        filepaths to some fixed width (8 by default).  This is turned off by
        default.
      save_relative_paths: If `True`, will write relative paths to the
        checkpoint state file. This is needed if the user wants to copy the
        checkpoint directory and reload from the copied directory.
      filename: If known at graph construction time, filename used for variable
        loading/saving.

    Raises:
      TypeError: If `var_list` is invalid.
      ValueError: If any of the keys or values in `var_list` are not unique.
      RuntimeError: If eager execution is enabled and`var_list` does not specify
        a list of variables to save.

    @compatibility(eager)
    When eager execution is enabled, `var_list` must specify a `list` or `dict`
    of variables to save. Otherwise, a `RuntimeError` will be raised.

    Although Saver works in some cases when executing eagerly, it is
    fragile. Please switch to `tf.train.Checkpoint` or
    `tf.keras.Model.save_weights`, which perform a more robust object-based
    saving. These APIs will load checkpoints written by `Saver`.
    @end_compatibility
    """
global _END_TIME_OF_LAST_WRITE
with _END_TIME_OF_LAST_WRITE_LOCK:
    if _END_TIME_OF_LAST_WRITE is None:
        _END_TIME_OF_LAST_WRITE = time.time()

if defer_build and var_list:
    raise ValueError(
        "If `var_list` is provided then build cannot be deferred. "
        "Either set defer_build=False or var_list=None.")
if context.executing_eagerly():
    logging.warning(
        "Saver is deprecated, please switch to tf.train.Checkpoint or "
        "tf.keras.Model.save_weights for training checkpoints. When "
        "executing eagerly variables do not necessarily have unique names, "
        "and so the variable.name-based lookups Saver performs are "
        "error-prone.")
    if var_list is None:
        raise RuntimeError(
            "When eager execution is enabled, `var_list` must specify a list "
            "or dict of variables to save")
self._var_list = var_list
self._reshape = reshape
self._sharded = sharded
self._max_to_keep = max_to_keep
self._keep_checkpoint_every_n_hours = keep_checkpoint_every_n_hours
self._name = name
self._restore_sequentially = restore_sequentially
self.saver_def = saver_def
self._builder = builder
self._is_built = False
self._allow_empty = allow_empty
self._is_empty = None
self._write_version = write_version
self._pad_step_number = pad_step_number
self._filename = filename
self._last_checkpoints = []
self._checkpoints_to_be_deleted = []
if context.executing_eagerly():
    self._next_checkpoint_time = (
        time.time() + self._keep_checkpoint_every_n_hours * 3600)
elif not defer_build:
    self.build()
if self.saver_def:
    self._check_saver_def()
    self._write_version = self.saver_def.version
self._save_relative_paths = save_relative_paths
# For compatibility with object-based checkpoints, we may build a second
# Saver to read the renamed keys.
self._object_restore_saver = None
