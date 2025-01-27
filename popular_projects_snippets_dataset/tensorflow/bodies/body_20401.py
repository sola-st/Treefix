# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/feature_column_v2.py
_TPUBaseEmbeddingColumn.__init__(
    self,
    categorical_column,
    max_sequence_length=max_sequence_length,
    learning_rate_fn=learning_rate_fn)
self._key = None
# If true, scope validation is skipped to allow the same column to be used
# in multiple variable scopes. By default, this is False, and we expect a
# 1:1 mapping between feature columns and scopes.
self._bypass_scope_validation = bypass_scope_validation
