# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
super(SequenceCategoricalColumnWithVocabularyFileTest, self).setUp()

vocab_strings = ['omar', 'stringer', 'marlo']
self._wire_vocabulary_file_name = self._write_vocab(vocab_strings,
                                                    'wire_vocabulary.txt')
self._wire_vocabulary_size = 3
