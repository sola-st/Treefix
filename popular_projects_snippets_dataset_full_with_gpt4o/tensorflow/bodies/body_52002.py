# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
super(VocabularyFileCategoricalColumnTest, self).setUp()

# Contains ints, Golden State Warriors jersey numbers: 30, 35, 11, 23, 22
self._warriors_vocabulary_file_name = test.test_src_dir_path(
    'python/feature_column/testdata/warriors_vocabulary.txt')
self._warriors_vocabulary_size = 5

# Contains strings, character names from 'The Wire': omar, stringer, marlo
self._wire_vocabulary_file_name = test.test_src_dir_path(
    'python/feature_column/testdata/wire_vocabulary.txt')
self._wire_vocabulary_size = 3
