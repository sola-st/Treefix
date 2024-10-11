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

builder = _LazyBuilder(features={'a': [[2], [3.]]})
column = Transformer()
self.assertEqual('Output', builder.get(column))
self.assertEqual('Output', builder.get(column))
