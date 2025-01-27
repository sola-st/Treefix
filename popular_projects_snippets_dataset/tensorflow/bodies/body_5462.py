# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/input_lib.py
self._input_workers = input_workers
super(DistributedDatasetV1, self).__init__(
    input_workers,
    strategy,
    dataset,
    num_replicas_in_sync=num_replicas_in_sync,
    input_context=input_context,
    options=options)
