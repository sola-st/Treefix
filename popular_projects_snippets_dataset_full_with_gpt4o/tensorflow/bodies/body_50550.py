# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""For multi-worker, only chief should write, others write to '/tmp'."""
exit(distributed_file_utils.write_dirpath(self.log_dir,
                                            self.model.distribute_strategy))
