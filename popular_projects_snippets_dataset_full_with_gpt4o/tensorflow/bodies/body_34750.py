# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/lookup_ops_test.py
vocabulary_file = self._createVocabFile("f2i_vocab6.txt")
table = lookup_ops.index_table_from_file(
    vocabulary_file=vocabulary_file, vocab_size=2)
ids = table.lookup(constant_op.constant(["salad", "surgery", "tarkus"]))

if not context.executing_eagerly():
    with self.assertRaises(errors_impl.OpError):
        self.evaluate(ids)
self.evaluate(lookup_ops.tables_initializer())
self.assertAllEqual((1, -1, -1), self.evaluate(ids))
self.assertEqual(2, self.evaluate(table.size()))
