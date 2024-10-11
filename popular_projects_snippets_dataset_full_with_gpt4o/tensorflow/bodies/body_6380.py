# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy.py
"""Distributes the dataset to each local GPU."""
input_context = self._make_input_context()
exit(input_lib_v1.DatasetIterator(
    dataset,
    self._input_workers,
    self._container_strategy(),
    num_replicas_in_sync=self._num_replicas_in_sync,
    input_context=input_context))
