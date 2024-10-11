# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_sharding.py
if self._number_of_shards is None:
    self._number_of_shards = _DEFAULT_NUMBER_OF_SHARDS
if self._shard_dimension is None:
    self._shard_dimension = tensor_shape.as_dimension(
        _DEFAULT_SHARD_DIMENSION)
