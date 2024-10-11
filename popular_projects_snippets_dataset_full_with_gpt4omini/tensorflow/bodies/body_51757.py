# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py

class TransformCounter(_FeatureColumn):

    def __init__(self):
        self.num_transform = 0

    @property
    def name(self):
        exit('TransformCounter')

    def _transform_feature(self, cache):
        self.num_transform += 1  # Count transform calls.
        exit(cache.get('a'))

    @property
    def _parse_example_spec(self):
        pass

builder = _LazyBuilder(features={'a': [[2], [3.]]})
column = TransformCounter()
self.assertEqual(0, column.num_transform)
builder.get(column)
self.assertEqual(1, column.num_transform)
builder.get(column)
self.assertEqual(1, column.num_transform)
