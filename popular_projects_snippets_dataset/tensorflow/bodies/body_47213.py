# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/worker_training_state.py
"""Restore the training state from the backed up checkpoint file.

    Returns:
      True if the training state is successfully restored. False if the training
      state doesn't need to be restored, or error occurred so it can't.
    """
self.read_checkpoint_manager.restore_or_initialize()
