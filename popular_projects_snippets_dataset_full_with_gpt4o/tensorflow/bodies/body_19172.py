# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_config.py
"""Adds a SparseFeature."""

if not feature.index_key:
    raise ValueError(f"Missing index_key for SparseFeature {feature}.")
if not feature.value_key:
    raise ValueError(f"Missing value_key for SparseFeature {feature}.")
if not feature.dtype:
    raise ValueError(f"Missing type for feature {key}. Received feature="
                     f"{feature}.")
index_keys = feature.index_key
if isinstance(index_keys, str):
    index_keys = [index_keys]
elif len(index_keys) > 1:
    tf_logging.warning("SparseFeature is a complicated feature config "
                       "and should only be used after careful "
                       "consideration of VarLenFeature.")
for index_key in sorted(index_keys):
    self._add_sparse_key(index_key, dtypes.int64)
self._add_sparse_key(feature.value_key, feature.dtype)
