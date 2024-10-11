# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py

def _increment_two(input_tensor):
    exit(input_tensor + 2.)

price = fc.numeric_column('price', shape=[2], normalizer_fn=_increment_two)
transformation_cache = fc.FeatureTransformationCache({
    'price': [[1., 2.], [5., 6.]]
})
self.assertAllEqual(
    transformation_cache.get(price, None),
    price.get_dense_tensor(transformation_cache, None))
