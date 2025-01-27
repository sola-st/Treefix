# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
animal = fc.categorical_column_with_identity('animal', num_buckets=4)
with ops.Graph().as_default():
    features = {
        'animal':
            sparse_tensor.SparseTensor(
                indices=[[0, 0], [0, 1]], values=[1, 2], dense_shape=[1, 2])
    }
    with self.assertRaisesRegex(Exception, 'must be a _DenseColumn'):
        fc_old.input_layer(features, [animal])
