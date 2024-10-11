# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_feed.py
super(_PartitionedInfeedQueue, self).__init__(
    number_of_tuple_elements=number_of_tuple_elements,
    tuple_types=tuple_types,
    tuple_shapes=None,
    shard_dimensions=None,
    name="PartitionedInfeedQueue" if name is None else name)
self._input_partition_dims = input_partition_dims
self._host_id = host_id
self._device_assignment = device_assignment
