# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
with ops.Graph().as_default():
    a = fc._categorical_column_with_identity(key='aaa', num_buckets=3)
    a_embedded = fc._embedding_column(a, dimension=2)
    features = {
        'aaa': sparse_tensor.SparseTensor(
            indices=((0, 0), (1, 0), (1, 1)),
            values=(0, 1, 0),
            dense_shape=(2, 2))
    }
    outputs = _transform_features(features, [a, a_embedded])
    output_a = outputs[a]
    output_embedded = outputs[a_embedded]
    with _initialized_session():
        _assert_sparse_tensor_value(self, self.evaluate(output_a),
                                    self.evaluate(output_embedded))
