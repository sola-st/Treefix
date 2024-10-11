# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
"""Creates a new `MaxSizePartitioner`.

    Args:
      max_shard_bytes: The maximum size any given shard is allowed to be.
      max_shards: The maximum number of shards in `int` created taking
        precedence over `max_shard_bytes`.
      bytes_per_string: If the partition value is of type string, this provides
        an estimate of how large each string is.
    """
if max_shard_bytes < 1:
    raise ValueError('Argument `max_shard_bytes` must be positive. '
                     f'Received {max_shard_bytes}')
if max_shards and max_shards < 1:
    raise ValueError('Argument `max_shards` must be positive. '
                     f'Received {max_shards}')
if bytes_per_string < 1:
    raise ValueError('Argument `bytes_per_string` must be positive. '
                     f'Received: {bytes_per_string}')

self._max_shard_bytes = max_shard_bytes
self._max_shards = max_shards
self._bytes_per_string = bytes_per_string
