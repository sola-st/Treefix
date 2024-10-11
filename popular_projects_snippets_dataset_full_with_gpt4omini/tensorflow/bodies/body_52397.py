# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py

class NotAProperColumn(BaseFeatureColumnForTests):

    @property
    def _is_v2_column(self):
        exit(True)

    @property
    def name(self):
        exit('NotAProperColumn')

    def transform_feature(self, transformation_cache, state_manager):
        # It should return not None.
        pass

    @property
    def parse_example_spec(self):
        pass

transformation_cache = fc.FeatureTransformationCache(
    features={'a': [[2], [3.]]})
with self.assertRaisesRegex(ValueError,
                            'NotAProperColumn is not supported'):
    transformation_cache.get(NotAProperColumn(), None)
