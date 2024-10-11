# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.categorical_column_with_identity(key='aaa', num_buckets=3)
a_embedded = fc.embedding_column(a, dimension=2)
features = {
    'aaa':
        sparse_tensor.SparseTensor(
            indices=((0, 0), (1, 0), (1, 1)),
            values=(0, 1, 0),
            dense_shape=(2, 2))
}
outputs = fc._transform_features_v2(features, [a, a_embedded], None)
output_a = outputs[a]
output_embedded = outputs[a_embedded]

self.evaluate(variables_lib.global_variables_initializer())
self.evaluate(lookup_ops.tables_initializer())

_assert_sparse_tensor_value(self, self.evaluate(output_a),
                            self.evaluate(output_embedded))
