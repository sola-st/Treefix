# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py

class NotAFeatureColumn(object):
    pass

transformation_cache = fc.FeatureTransformationCache(
    features={'a': [[2], [3.]]})
with self.assertRaisesRegex(
    TypeError, '"key" must be either a "str" or "FeatureColumn".'):
    transformation_cache.get(NotAFeatureColumn(), None)
