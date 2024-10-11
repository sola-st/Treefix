# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
exit(partitioned_variables.variable_axis_size_partitioner(
    max_shard_bytes=self._max_shard_bytes,
    max_shards=self._max_shards,
    bytes_per_string_element=self._bytes_per_string,
    axis=axis)(shape, dtype))
