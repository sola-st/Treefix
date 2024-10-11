# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
default_value = -42
vocabulary_file = self._createVocabFile("f2i_vocab4.txt")
table = lookup_ops.index_table_from_file(
    vocabulary_file=vocabulary_file, default_value=default_value)
ids = table.lookup(constant_op.constant(["salad", "surgery", "tarkus"]))

if not context.executing_eagerly():
    with self.assertRaises(errors_impl.OpError):
        self.evaluate(ids)
self.evaluate(lookup_ops.tables_initializer())
self.assertAllEqual((1, 2, default_value), self.evaluate(ids))
