# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
column = fc.categorical_column_with_vocabulary_list(
    key='aaa',
    vocabulary_list=('omar', 'stringer', 'marlo'),
    num_oov_buckets=100)
inputs = sparse_tensor.SparseTensorValue(
    indices=((0, 0), (1, 0), (1, 1), (1, 2)),
    values=('marlo', 'skywalker', 'omar', 'heisenberg'),
    dense_shape=(2, 3))
id_weight_pair = column.get_sparse_tensors(
    fc.FeatureTransformationCache({
        'aaa': inputs
    }), None)
self.assertIsNone(id_weight_pair.weight_tensor)

self.evaluate(variables_lib.global_variables_initializer())
self.evaluate(lookup_ops.tables_initializer())

_assert_sparse_tensor_value(
    self,
    sparse_tensor.SparseTensorValue(
        indices=inputs.indices,
        values=np.array((2, 33, 0, 62), dtype=np.int64),
        dense_shape=inputs.dense_shape),
    self.evaluate(id_weight_pair.id_tensor))
