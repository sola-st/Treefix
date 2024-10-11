# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/worker_training_state.py
"""Back up the current state of training into a checkpoint file.

    Args:
      epoch: The current epoch information to be saved.
    """
backend.set_value(self._ckpt_saved_epoch, epoch)
# Save the model plus CKPT_SAVED_EPOCH variable.
if self.write_checkpoint_manager.save():
    distributed_file_utils.remove_temp_dirpath(
        self.write_checkpoint_manager.directory,
        self._model.distribute_strategy)
