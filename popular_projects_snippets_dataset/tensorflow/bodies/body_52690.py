# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
animal = fc.indicator_column(
    fc.categorical_column_with_hash_bucket('animal', 4))
transformation_cache = fc.FeatureTransformationCache({
    'animal': ['fox', 'fox']
})
output = transformation_cache.get(animal, None)

self.assertAllEqual([[0., 0., 1., 0.], [0., 0., 1., 0.]],
                    self.evaluate(output))
