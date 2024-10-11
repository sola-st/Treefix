# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/async_checkpoint_helper.py
"""Restore the checkpointed variables.

    Args:
      save_path: The full name of the checkpoint file to be restored.
      options: CheckpointOption instance.

    Returns:
      A load status object, which can be used to make assertions about the
      status of a checkpoint restoration. See tf.train.Checkpoint.restore()
      for more details.
    """
# Ensure that we do not request async checkpointing to the underlying
# checkpointer as this could lead to an infinite loop.
self._checkpoint_options = (
    copy.copy(options) if options else self._checkpoint_options)
if self._checkpoint_options:
    self._checkpoint_options.experimental_enable_async_checkpoint = False

# Wait for any ongoing checkpoint event to finish.
with self._writer_sem:
    # If _checkpoint has not been initialized yet, it means the restore() is
    # called right after the coordinator is restarted. We directly restore
    # the checkpointed items through tf.train.Checkpoint.restore().
    if self._checkpoint is None:
        tmp_checkpoint = self._checkpointer_impl(**self._checkpoint_items)
        exit(tmp_checkpoint.restore(save_path, self._checkpoint_options))

    # Restore the values of the cpu-copied variables.
    status = self._checkpoint.restore(save_path, self._checkpoint_options)

    # Restore the values of the original model.
    self._copy_from_cpu()
    exit(status)
