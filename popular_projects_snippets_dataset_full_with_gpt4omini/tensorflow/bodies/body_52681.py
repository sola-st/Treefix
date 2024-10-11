# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
bucketized_price = fc.bucketized_column(
    fc.numeric_column('price'), boundaries=[0, 2, 4, 6])
hashed_sparse = fc.categorical_column_with_hash_bucket('wire', 10)
with ops.Graph().as_default():
    features = {
        'price': [[-1.], [5.]],
        'wire':
            sparse_tensor.SparseTensor(
                values=['omar', 'stringer', 'marlo'],
                indices=[[0, 0], [1, 0], [1, 1]],
                dense_shape=[2, 2])
    }
    transformed = fc._transform_features_v2(
        features, [bucketized_price, hashed_sparse], None)

    self.evaluate(variables_lib.global_variables_initializer())
    self.evaluate(lookup_ops.tables_initializer())

    self.assertIn(bucketized_price.name, transformed[bucketized_price].name)
    self.assertAllEqual([[0], [3]],
                        self.evaluate(transformed[bucketized_price]))
    self.assertIn(hashed_sparse.name, transformed[hashed_sparse].name)
    self.assertAllEqual([6, 4, 1],
                        self.evaluate(transformed[hashed_sparse].values))
