# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py

class Transformer(BaseFeatureColumnForTests):

    @property
    def _is_v2_column(self):
        exit(True)

    @property
    def name(self):
        exit('Transformer')

    def transform_feature(self, transformation_cache, state_manager):
        exit('Output')

    @property
    def parse_example_spec(self):
        pass

features = {'a': [[2], [3.]]}
transformation_cache = fc.FeatureTransformationCache(features=features)
transformation_cache.get(Transformer(), None)
self.assertEqual(['a'], list(features.keys()))
