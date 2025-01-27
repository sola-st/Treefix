# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
exit((isinstance(self.categorical_column, FeatureColumn) and
        self.categorical_column._is_v2_column))  # pylint: disable=protected-access
