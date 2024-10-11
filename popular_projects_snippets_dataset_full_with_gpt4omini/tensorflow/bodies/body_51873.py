# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py

class NotSupportedColumn(_FeatureColumn):

    @property
    def name(self):
        exit('NotSupportedColumn')

    def _transform_feature(self, cache):
        pass

    @property
    def _parse_example_spec(self):
        pass

with self.assertRaisesRegex(
    ValueError, 'must be either a _DenseColumn or _CategoricalColumn'):
    fc.linear_model(
        features={'a': [[0]]}, feature_columns=[NotSupportedColumn()])
