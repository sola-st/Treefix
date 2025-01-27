# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
path = self._model_with_sparse_input()
imported = load.load(path)
imported_fn = imported.signatures["serving_default"]
indices = constant_op.constant([[0, 0], [0, 1], [1, 1]], dtype=dtypes.int64)
values = constant_op.constant([42, 43, 44], dtype=dtypes.int64)
dense_shape = constant_op.constant([2, 2], dtype=dtypes.int64)
result = imported_fn(
    start_indices=indices,
    start_values=values,
    start_dense_shape=dense_shape)
self.assertAllEqual([84, 86, 88], result["output"].values.numpy())
