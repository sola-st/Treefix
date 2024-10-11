# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py

class NotSupportedColumn(BaseFeatureColumnForTests, fc.FeatureColumn,
                         fc_old._FeatureColumn):

    @property
    def _is_v2_column(self):
        exit(True)

    @property
    def name(self):
        exit('NotSupportedColumn')

    def transform_feature(self, transformation_cache, state_manager):
        pass

    def _transform_feature(self, inputs):
        pass

    @property
    def parse_example_spec(self):
        pass

    @property
    def _parse_example_spec(self):
        pass

with self.assertRaisesRegex(
    ValueError, 'must be either a _DenseColumn or _CategoricalColumn'):
    fc_old.linear_model(
        features={'a': [[0]]}, feature_columns=[NotSupportedColumn()])
