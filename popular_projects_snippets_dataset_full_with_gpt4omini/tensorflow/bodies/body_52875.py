# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
self._dimension = dimension
self._initializer = initializer
self._ckpt_to_load_from = ckpt_to_load_from
self._tensor_name_in_ckpt = tensor_name_in_ckpt
self._num_buckets = num_buckets
self._trainable = trainable
self._name = name
self._use_safe_embedding_lookup = use_safe_embedding_lookup
# Map from graph keys to embedding_weight variables.
self._embedding_weights = {}
