# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
animal = fc._indicator_column(
    fc._categorical_column_with_identity('animal', num_buckets=4))
with ops.Graph().as_default():
    features = {
        'animal':
            sparse_tensor.SparseTensor(
                indices=[[0, 0], [0, 1]], values=[1, 2], dense_shape=[1, 2])
    }
    net = fc.input_layer(features, [animal])
    with _initialized_session():
        self.assertAllClose([[0., 1., 1., 0.]], self.evaluate(net))
