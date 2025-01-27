# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
transformation_cache = fc.FeatureTransformationCache(
    features={'a': [[2], [3.]]})
with self.assertRaisesRegex(ValueError,
                            'bbb is not in features dictionary'):
    transformation_cache.get('bbb', None)
with self.assertRaisesRegex(ValueError,
                            'bbb is not in features dictionary'):
    transformation_cache.get(u'bbb', None)
