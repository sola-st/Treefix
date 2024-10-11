# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/worker_training_state.py
"""Delete the backup directories.

    Delete the backup directories which should not exist after `fit()`
    successfully finishes.
    """
if self.write_checkpoint_manager is self.read_checkpoint_manager:
    try:
        file_io.delete_recursively_v2(self.write_checkpoint_manager.directory)
    except errors.NotFoundError:
        pass
