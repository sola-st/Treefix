# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocabulary_file = constant_op.constant(
    self._createVocabFile("zero_vocab_tensor.txt"))
self.assertRaisesRegex(
    ValueError, "`vocab_size` must be greater than 0, got 0 for "
    "vocabulary_file: .*zero_vocab_tensor.txt",
    lookup_ops.index_table_from_file,
    vocabulary_file=vocabulary_file,
    vocab_size=0)
