# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocabulary_path = self._createVocabFile("i2f_vocab1.txt")
# vocabulary_file supports string and tensor
type_funcs = [str, constant_op.constant]
for type_func in type_funcs:
    vocabulary_file = type_func(vocabulary_path)
    table = lookup_ops.index_to_string_table_from_file(
        vocabulary_file=vocabulary_file)
    features = table.lookup(constant_op.constant([0, 1, 2, 3], dtypes.int64))
    if not context.executing_eagerly():
        with self.assertRaises(errors_impl.OpError):
            self.evaluate(features)
    self.evaluate(lookup_ops.tables_initializer())
    self.assertAllEqual((b"brain", b"salad", b"surgery", b"UNK"),
                        self.evaluate(features))
