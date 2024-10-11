# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Deletes tmp write directories for multi-worker."""
distributed_file_utils.remove_temp_dirpath(self.log_dir,
                                           self.model.distribute_strategy)
