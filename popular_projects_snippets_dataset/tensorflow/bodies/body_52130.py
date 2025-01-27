# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    a = fc._categorical_column_with_identity(key='aaa', num_buckets=3)
    b = fc._categorical_column_with_identity(key='bbb', num_buckets=3)
    a_embedded, b_embedded = fc_new.shared_embedding_columns([a, b],
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
    outputs = _transform_features(features, [a, a_embedded, b, b_embedded])
    output_a = outputs[a]
    output_a_embedded = outputs[a_embedded]
    output_b = outputs[b]
    output_b_embedded = outputs[b_embedded]
    with _initialized_session():
        _assert_sparse_tensor_value(self, self.evaluate(output_a),
                                    self.evaluate(output_a_embedded))
        _assert_sparse_tensor_value(self, self.evaluate(output_b),
                                    self.evaluate(output_b_embedded))
