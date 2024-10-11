# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
column = fc.weighted_categorical_column(
    categorical_column=fc_old._categorical_column_with_identity(
        key='ids', num_buckets=3),
    weight_feature_key='values')
self.assertFalse(column._is_v2_column)
