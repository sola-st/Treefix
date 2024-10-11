# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management.py
"""Configure a `CheckpointManager` for use in `directory`.

    If a `CheckpointManager` was previously used in `directory`, its
    state will be restored. This includes the list of managed checkpoints and
    the timestamp bookkeeping necessary to support
    `keep_checkpoint_every_n_hours`. The behavior of the new `CheckpointManager`
    will be the same as the previous `CheckpointManager`, including cleaning up
    existing checkpoints if appropriate.

    Checkpoints are only considered for deletion just after a new checkpoint has
    been added. At that point, `max_to_keep` checkpoints will remain in an
    "active set". Once a checkpoint is preserved by
    `keep_checkpoint_every_n_hours` it will not be deleted by this
    `CheckpointManager` or any future `CheckpointManager` instantiated in
    `directory` (regardless of the new setting of
    `keep_checkpoint_every_n_hours`). The `max_to_keep` checkpoints in the
    active set may be deleted by this `CheckpointManager` or a future
    `CheckpointManager` instantiated in `directory` (subject to its
    `max_to_keep` and `keep_checkpoint_every_n_hours` settings).

    `CheckpointManager` can be also used for initializing the model if
    there is no checkpoints for restoring in `directory`. An example usage is:

    >>> import tempfile

    >>> tmp_dir = tempfile.mkdtemp()
    >>> checkpoint = tf.train.Checkpoint()
    >>> init_path = checkpoint.save(os.path.join(tmp_dir, 'init'))

    >>> def init_fn():
    ...   # Partially restore the checkpoint from `init_path`.
    ...   checkpoint.restore(init_path)

    >>> manager = tf.train.CheckpointManager(
    ...     checkpoint,
    ...     directory=os.path.join(tmp_dir, 'ckpt'),
    ...     max_to_keep=None,
    ...     init_fn=init_fn)
    >>> # `restore_or_initialize` will call `init_fn` if there is no existing
    >>> # checkpoint in `directory`.
    >>> manager.restore_or_initialize()

    Args:
      checkpoint: The `tf.train.Checkpoint` instance to save and manage
        checkpoints for.
      directory: The path to a directory in which to write checkpoints. A
        special file named "checkpoint" is also written to this directory (in a
        human-readable text format) which contains the state of the
        `CheckpointManager`.
      max_to_keep: An integer, the number of checkpoints to keep. Unless
        preserved by `keep_checkpoint_every_n_hours`, checkpoints will be
        deleted from the active set, oldest first, until only `max_to_keep`
        checkpoints remain. If `None`, no checkpoints are deleted and everything
        stays in the active set. Note that `max_to_keep=None` will keep all
        checkpoint paths in memory and in the checkpoint state protocol buffer
        on disk.
      keep_checkpoint_every_n_hours: Upon removal from the active set, a
        checkpoint will be preserved if it has been at least
        `keep_checkpoint_every_n_hours` since the last preserved checkpoint. The
        default setting of `None` does not preserve any checkpoints in this way.
      checkpoint_name: Custom name for the checkpoint file.
      step_counter: A `tf.Variable` instance for checking the current step
        counter value, in case users want to save checkpoints every N steps.
      checkpoint_interval: An integer, indicates the minimum step interval
        between two checkpoints.
      init_fn: Callable. A function to do customized intialization if no
        checkpoints are in the directory.

    Raises:
      ValueError: If `max_to_keep` is not a positive integer.
    """
self._checkpoint = checkpoint
self._save_counter_assign = None
if max_to_keep is not None and max_to_keep <= 0:
    raise ValueError(
        ("Expected a positive integer or `None` for `max_to_keep`, "
         "got %d.")
        % (max_to_keep,))
self._max_to_keep = max_to_keep
self._keep_checkpoint_every_n_hours = keep_checkpoint_every_n_hours
if isinstance(directory, os.PathLike):
    directory = os.fspath(directory)
self._directory = directory
self._checkpoint_prefix = os.path.join(directory, checkpoint_name)
self._init_fn = init_fn

if checkpoint_interval is not None:
    if step_counter is None:
        raise ValueError("`step_counter` should be passed if "
                         "`checkpoint_interval` is not None.")
    self._last_checkpoint_step = None
    self._step_counter = step_counter
self._checkpoint_interval = checkpoint_interval

recovered_state = get_checkpoint_state(directory)
current_clock = time.time()
self._maybe_delete = collections.OrderedDict()
if recovered_state is None:
    self._latest_checkpoint = None
    # Set the clock back slightly to avoid race conditions when quickly
    # re-creating a CheckpointManager.
    self._last_preserved_timestamp = current_clock - 1.
else:
    self._latest_checkpoint = recovered_state.model_checkpoint_path
    self._last_preserved_timestamp = recovered_state.last_preserved_timestamp
    if current_clock < self._last_preserved_timestamp:
        # Time seems to have reversed itself. In addition to this warning, we'll
        # min() saved checkpoint timestamps with the current time to ensure that
        # old checkpoints don't get deleted accidentally.
        logging.warning(
            ("time.time() returned a value %f seconds behind the last "
             "preserved checkpoint timestamp.")
            % (self._last_preserved_timestamp - current_clock,))
        self._last_preserved_timestamp = current_clock
    all_timestamps = recovered_state.all_model_checkpoint_timestamps
    all_paths = recovered_state.all_model_checkpoint_paths
    del recovered_state  # Uses modified values from now on
    if not all_timestamps:
        all_timestamps = [self._last_preserved_timestamp] * len(all_paths)

    for filename, timestamp in zip(all_paths, all_timestamps):
        timestamp = min(timestamp, current_clock)
        if timestamp > self._last_preserved_timestamp:
            self._maybe_delete[filename] = timestamp
