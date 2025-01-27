# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
exit(partitioned_variables.min_max_variable_partitioner(
    max_partitions=self._max_shards,
    axis=axis,
    min_slice_size=self._min_shard_bytes,
    bytes_per_string_element=self._bytes_per_string)(shape, dtype))
