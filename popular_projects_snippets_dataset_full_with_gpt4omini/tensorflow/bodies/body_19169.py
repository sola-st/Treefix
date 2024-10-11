# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_config.py
"""Adds the specified feature to this ParseOpParams."""
if isinstance(feature, VarLenFeature):
    self._add_varlen_feature(key, feature)
elif isinstance(feature, SparseFeature):
    self._add_sparse_feature(key, feature)
elif isinstance(feature, FixedLenFeature):
    self._add_fixed_len_feature(key, feature)
elif isinstance(feature, FixedLenSequenceFeature):
    self._add_fixed_len_sequence_feature(key, feature)
elif isinstance(feature, RaggedFeature):
    self._add_ragged_feature(key, feature)
else:
    raise ValueError(f"Invalid feature {key}:{feature}.")
