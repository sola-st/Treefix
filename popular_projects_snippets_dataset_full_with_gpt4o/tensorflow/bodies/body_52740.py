# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# SharedEmbeddingColumns are graph-only
with ops.Graph().as_default():
    a = fc.categorical_column_with_identity(key='aaa', num_buckets=3)
    b = fc.categorical_column_with_identity(key='bbb', num_buckets=3)
    a_embedded, b_embedded = fc.shared_embedding_columns_v2([a, b],
                                                            dimension=2)
    features = {
        'aaa':
            sparse_tensor.SparseTensor(
                indices=((0, 0), (1, 0), (1, 1)),
                values=(0, 1, 0),
                dense_shape=(2, 2)),
        'bbb':
            sparse_tensor.SparseTensor(
                indices=((0, 0), (1, 0), (1, 1)),
                values=(1, 2, 1),
                dense_shape=(2, 2)),
    }
    outputs = fc._transform_features_v2(features,
                                        [a, a_embedded, b, b_embedded], None)
    output_a = outputs[a]
    output_a_embedded = outputs[a_embedded]
    output_b = outputs[b]
    output_b_embedded = outputs[b_embedded]

    self.evaluate(variables_lib.global_variables_initializer())
    self.evaluate(lookup_ops.tables_initializer())

    _assert_sparse_tensor_value(self, self.evaluate(output_a),
                                self.evaluate(output_a_embedded))
    _assert_sparse_tensor_value(self, self.evaluate(output_b),
                                self.evaluate(output_b_embedded))
