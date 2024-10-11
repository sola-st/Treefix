# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
animal = fc.indicator_column(
    fc.categorical_column_with_identity('animal', num_buckets=4))
transformation_cache = fc.FeatureTransformationCache({
    'animal':
        sparse_tensor.SparseTensor(
            indices=[[0, 0], [0, 1]], values=[1, 2], dense_shape=[1, 2])
})
output = transformation_cache.get(animal, None)

self.assertAllEqual([[0., 1., 1., 0.]], self.evaluate(output))
