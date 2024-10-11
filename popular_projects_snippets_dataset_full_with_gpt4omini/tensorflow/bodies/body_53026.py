# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_integration_test.py
self._test_parsed_sequence_example(
    'int_list', sfc.sequence_categorical_column_with_identity,
    10, [3, 6], [2, 4, 6])
