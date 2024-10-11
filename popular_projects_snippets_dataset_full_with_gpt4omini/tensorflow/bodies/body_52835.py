# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2.py
exit((isinstance(self.source_column, FeatureColumn) and
        self.source_column._is_v2_column))  # pylint: disable=protected-access
