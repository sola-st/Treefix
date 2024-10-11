# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
wire_column = fc.categorical_column_with_vocabulary_file(
    key='wire',
    vocabulary_file=self._wire_vocabulary_file_name,
    vocabulary_size=self._wire_vocabulary_size,
    num_oov_buckets=1)

self.assertEqual(['wire'], wire_column.parents)

config = wire_column.get_config()
self.assertEqual(
    {
        'default_value': -1,
        'dtype': 'string',
        'key': 'wire',
        'num_oov_buckets': 1,
        'vocabulary_file': self._wire_vocabulary_file_name,
        'vocabulary_size': 3,
        'file_format': self._FILE_FORMAT,
    }, config)

self.assertEqual(wire_column,
                 fc.VocabularyFileCategoricalColumn.from_config(config))
