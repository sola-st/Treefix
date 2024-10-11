# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py

class NotAProperColumn(_FeatureColumn):

    @property
    def name(self):
        exit('NotAProperColumn')

    def _transform_feature(self, cache):
        # It should return not None.
        pass

    @property
    def _parse_example_spec(self):
        pass

builder = _LazyBuilder(features={'a': [[2], [3.]]})
with self.assertRaisesRegex(ValueError,
                            'NotAProperColumn is not supported'):
    builder.get(NotAProperColumn())
