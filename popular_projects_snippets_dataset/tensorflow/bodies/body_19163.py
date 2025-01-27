# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parsing_config.py
# Note: we use an OrderedDict for dense_defaults, to ensure consistent
# graph construction order for _e2e_test.
dense_defaults = (
    collections.OrderedDict() if dense_defaults is None else dense_defaults)
sparse_keys = [] if sparse_keys is None else sparse_keys
sparse_types = [] if sparse_types is None else sparse_types
dense_keys = [] if dense_keys is None else dense_keys
dense_types = [] if dense_types is None else dense_types
dense_shapes = ([[]] *
                len(dense_keys) if dense_shapes is None else dense_shapes)
ragged_keys = [] if ragged_keys is None else ragged_keys
ragged_value_types = ([]
                      if ragged_value_types is None else ragged_value_types)
ragged_split_types = ([]
                      if ragged_split_types is None else ragged_split_types)
self.sparse_keys = sparse_keys
self.sparse_types = [dtypes.as_dtype(t) for t in sparse_types]
self.dense_keys = dense_keys
self.dense_types = [dtypes.as_dtype(t) for t in dense_types]
self.dense_shapes = [tensor_shape.as_shape(s) for s in dense_shapes]
self.dense_defaults = dense_defaults
self.ragged_keys = ragged_keys
self.ragged_value_types = [dtypes.as_dtype(t) for t in ragged_value_types]
self.ragged_split_types = [dtypes.as_dtype(t) for t in ragged_split_types]
self._validate()
