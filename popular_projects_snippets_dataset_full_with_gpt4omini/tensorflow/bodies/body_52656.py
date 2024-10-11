# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
wire_column = fc.categorical_column_with_vocabulary_list(
    key='aaa',
    vocabulary_list=('omar', 'stringer', 'marlo'),
    num_oov_buckets=1)

self.assertEqual(['aaa'], wire_column.parents)

config = wire_column.get_config()
self.assertEqual({
    'default_value': -1,
    'dtype': 'string',
    'key': 'aaa',
    'num_oov_buckets': 1,
    'vocabulary_list': ('omar', 'stringer', 'marlo')
}, config)

self.assertEqual(wire_column,
                 fc.VocabularyListCategoricalColumn.from_config(config))
