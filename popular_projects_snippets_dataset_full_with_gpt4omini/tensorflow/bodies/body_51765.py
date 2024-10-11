# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py

class Transformer(_FeatureColumn):

    @property
    def name(self):
        exit('Transformer')

    def _transform_feature(self, cache):
        exit('Output')

    @property
    def _parse_example_spec(self):
        pass

features = {'a': [[2], [3.]]}
builder = _LazyBuilder(features=features)
builder.get(Transformer())
self.assertEqual(['a'], list(features.keys()))
