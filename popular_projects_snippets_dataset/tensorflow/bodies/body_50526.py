# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
# Remove the checkpoint directory in multi-worker training where this worker
# should not checkpoint. It is a dummy directory previously saved for sync
# distributed training.
distributed_file_utils.remove_temp_dir_with_filepath(
    self._write_filepath, self.model.distribute_strategy)
