# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
# TODO(ispir/cassandrax): Swith to categorical_column_with_keys when ready.
animal = fc.indicator_column(
    fc.categorical_column_with_hash_bucket('animal', 4))
transformation_cache = fc.FeatureTransformationCache({
    'animal':
        sparse_tensor.SparseTensor(
            indices=[[0, 0], [1, 0]],
            values=['fox', 'fox'],
            dense_shape=[2, 1])
})
output = transformation_cache.get(animal, None)

self.assertAllEqual([[0., 0., 1., 0.], [0., 0., 1., 0.]],
                    self.evaluate(output))
