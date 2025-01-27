# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocabulary_file = self._createVocabFile("f2i_vocab7.txt")
table = lookup_ops.index_to_string_table_from_file(
    vocabulary_file=vocabulary_file, vocab_size=3)
features = table.lookup(constant_op.constant([1, 2, 4], dtypes.int64))

if not context.executing_eagerly():
    with self.assertRaises(errors_impl.OpError):
        self.evaluate(features)
self.evaluate(lookup_ops.tables_initializer())
self.assertAllEqual((b"salad", b"surgery", b"UNK"), self.evaluate(features))
