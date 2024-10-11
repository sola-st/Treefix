# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
price = fc.numeric_column('price')
bucketized_price = fc.bucketized_column(price, boundaries=[0, 1])
transformation_cache = fc.FeatureTransformationCache({
    'price':
        sparse_tensor.SparseTensor(
            indices=[[0, 0]], values=[0.3], dense_shape=[1, 1])
})
with self.assertRaisesRegex(ValueError, 'must be a Tensor'):
    bucketized_price.transform_feature(transformation_cache, None)
