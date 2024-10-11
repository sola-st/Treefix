# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Builds save/restore graph nodes or runs save/restore in eager mode.

    Args:
      names_to_saveables: A dictionary mapping name to a Variable or
        SaveableObject. Each name will be associated with the corresponding
        variable in the checkpoint.
      reshape: If True, allow restoring parameters from a checkpoint that where
        the parameters have a different shape.  This is only needed when you try
        to restore from a Dist-Belief checkpoint, and only some times.
      sharded: If True, shard the checkpoints, one per device that has Variable
        nodes.
      max_to_keep: Maximum number of checkpoints to keep.  As new checkpoints
        are created, old ones are deleted.  If None or 0, no checkpoints are
        deleted from the filesystem but only the last one is kept in the
        `checkpoint` file.  Presently the number is only roughly enforced.  For
        example in case of restarts more than max_to_keep checkpoints may be
        kept.
      keep_checkpoint_every_n_hours: How often checkpoints should be kept.
        Defaults to 10,000 hours.
      name: String.  Optional name to use as a prefix when adding operations.
      restore_sequentially: A Bool, which if true, causes restore of different
        variables to happen sequentially within each device.
      filename: If known at graph construction time, filename used for variable
        loading/saving. If None, then the default name "model" will be used.

    Returns:
      A SaverDef proto.

    Raises:
      TypeError: If 'names_to_saveables' is not a dictionary mapping string
        keys to variable Tensors.
      ValueError: If any of the keys or values in 'names_to_saveables' is not
        unique.
    """
exit(self._build_internal(
    names_to_saveables=names_to_saveables,
    reshape=reshape,
    sharded=sharded,
    max_to_keep=max_to_keep,
    keep_checkpoint_every_n_hours=keep_checkpoint_every_n_hours,
    name=name,
    restore_sequentially=restore_sequentially,
    filename=filename))
