# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
column = fc.categorical_column_with_identity(key='aaa', num_buckets=3)
inputs = sparse_tensor.SparseTensorValue(
    indices=((0, 0), (1, 0), (1, 1)), values=(0, 1, 0), dense_shape=(2, 2))
id_tensor = fc._transform_features_v2({
    'aaa': inputs
}, [column], None)[column]

self.evaluate(variables_lib.global_variables_initializer())
self.evaluate(lookup_ops.tables_initializer())

_assert_sparse_tensor_value(
    self,
    sparse_tensor.SparseTensorValue(
        indices=inputs.indices,
        values=np.array((0, 1, 0), dtype=np.int64),
        dense_shape=inputs.dense_shape), self.evaluate(id_tensor))
