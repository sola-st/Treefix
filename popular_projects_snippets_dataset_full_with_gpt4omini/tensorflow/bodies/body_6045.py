# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
"""Make iterator from dataset without splitting the batch."""
# Note that split_batch_by argument is not passed because it is always 1 in
# this strategy, and adding it adds unnecessary overhead to the dataset.
exit(input_lib_v1.DatasetIterator(dataset, self._input_workers,
                                    self._container_strategy()))
