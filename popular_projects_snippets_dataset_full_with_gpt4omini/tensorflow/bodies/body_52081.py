# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
bucketized_price = fc._bucketized_column(
    fc._numeric_column('price'), boundaries=[0, 2, 4, 6])
hashed_sparse = fc._categorical_column_with_hash_bucket('wire', 10)
with ops.Graph().as_default():
    features = {
        'price': [[-1.], [5.]],
        'wire':
            sparse_tensor.SparseTensor(
                values=['omar', 'stringer', 'marlo'],
                indices=[[0, 0], [1, 0], [1, 1]],
                dense_shape=[2, 2])
    }
    transformed = _transform_features(features,
                                      [bucketized_price, hashed_sparse])
    with _initialized_session():
        self.assertIn(bucketized_price.name, transformed[bucketized_price].name)
        self.assertAllEqual([[0], [3]], transformed[bucketized_price])
        self.assertIn(hashed_sparse.name, transformed[hashed_sparse].name)
        self.assertAllEqual([6, 4, 1], transformed[hashed_sparse].values)
