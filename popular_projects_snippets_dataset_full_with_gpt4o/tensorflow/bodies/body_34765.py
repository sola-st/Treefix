# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocabulary_file = self._createVocabFile(
    "f2i_vocab1.txt", values=("brain\t300", "salad\t20", "surgery\t1"))
table = lookup_ops.index_to_string_table_from_file(
    vocabulary_file=vocabulary_file,
    key_column_index=lookup_ops.TextFileIndex.LINE_NUMBER,
    value_column_index=0)
features = table.lookup(constant_op.constant([0, 1, 2, 3], dtypes.int64))
if not context.executing_eagerly():
    with self.assertRaises(errors_impl.OpError):
        self.evaluate(features)
self.evaluate(lookup_ops.tables_initializer())
self.assertAllEqual((b"brain", b"salad", b"surgery", b"UNK"),
                    self.evaluate(features))
