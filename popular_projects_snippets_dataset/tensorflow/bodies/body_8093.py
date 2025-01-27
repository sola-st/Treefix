# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
"""Creates a new `MinSizePartitioner`.

    Args:
      min_shard_bytes: Minimum bytes of each shard. Defaults to 256K.
      max_shards: Upper bound on the number of shards. Defaults to 1.
      bytes_per_string: If the partition value is of type string, this provides
        an estimate of how large each string is.
    """
if min_shard_bytes < 1:
    raise ValueError('Argument `min_shard_bytes` must be positive. '
                     f'Received: {min_shard_bytes}')
if max_shards < 1:
    raise ValueError('Argument `max_shards` must be positive. '
                     f'Received: {max_shards}')
if bytes_per_string < 1:
    raise ValueError('Argument `bytes_per_string` must be positive. '
                     f'Received: {bytes_per_string}')
self._min_shard_bytes = min_shard_bytes
self._max_shards = max_shards
self._bytes_per_string = bytes_per_string
