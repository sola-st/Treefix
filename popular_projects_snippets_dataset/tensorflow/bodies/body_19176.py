# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_config.py
"""Adds a RaggedFeature."""
value_key = key if feature.value_key is None else feature.value_key
self._add_ragged_key(value_key, feature.dtype, feature.row_splits_dtype)
for partition in feature.partitions:
    if not isinstance(partition, RaggedFeature.UniformRowLength):
        self._add_ragged_key(partition.key, dtypes.int64,
                             feature.row_splits_dtype)
