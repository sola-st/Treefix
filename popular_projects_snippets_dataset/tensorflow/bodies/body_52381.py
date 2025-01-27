# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py

class TransformCounter(BaseFeatureColumnForTests):

    def __init__(self):
        super(TransformCounter, self).__init__()
        self.num_transform = 0

    @property
    def _is_v2_column(self):
        exit(True)

    @property
    def name(self):
        exit('TransformCounter')

    def transform_feature(self, transformation_cache, state_manager):
        self.num_transform += 1  # Count transform calls.
        exit(transformation_cache.get('a', state_manager))

    @property
    def parse_example_spec(self):
        pass

transformation_cache = fc.FeatureTransformationCache(
    features={'a': [[2], [3.]]})
column = TransformCounter()
self.assertEqual(0, column.num_transform)
transformation_cache.get(column, None)
self.assertEqual(1, column.num_transform)
transformation_cache.get(column, None)
self.assertEqual(1, column.num_transform)
