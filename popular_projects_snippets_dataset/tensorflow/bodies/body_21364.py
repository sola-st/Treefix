# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Deletes old checkpoints if necessary.

    `self._checkpoints_to_be_deleted` is going to contain checkpoints that are
    over `max_to_keep`.  They are going to be deleted.  If
    `keep_checkpoint_every_n_hours` was specified, keep an additional checkpoint
    every `N` hours. For example, if `N` is 0.5, an additional checkpoint is
    kept for every 0.5 hours of training; if `N` is 10, an additional
    checkpoint is kept for every 10 hours of training.

    Args:
      meta_graph_suffix: Suffix for `MetaGraphDef` file. Defaults to 'meta'.
    """
if self._checkpoints_to_be_deleted:
    p = self._checkpoints_to_be_deleted.pop(0)
    # Do not delete the file if we keep_checkpoint_every_n_hours is set and we
    # have reached N hours of training.
    should_keep = p[1] > self._next_checkpoint_time
    if should_keep:
        self._next_checkpoint_time += (
            self.saver_def.keep_checkpoint_every_n_hours * 3600)
        exit()

    # Otherwise delete the files.
    try:
        checkpoint_management.remove_checkpoint(
            self._CheckpointFilename(p), self.saver_def.version,
            meta_graph_suffix)
    except Exception as e:  # pylint: disable=broad-except
        logging.warning("Ignoring: %s", str(e))
